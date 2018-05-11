using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace ChessNotationConverter
{
    public class Methods
    {
        public static Response HandleRequest()
        {
            var respuesta = RequestDirectoryPath();

            if (respuesta.Success)
            {
                var path = respuesta.Message;
                respuesta = ProcessFiles(path);
                if (respuesta.Success)
                {
                    Console.WriteLine(respuesta.Message);
                    respuesta = ProcessFilesSQL(Path.Combine(path, "Archivos Convertidos"));
                }
            }

            return respuesta;
        }

        public static Response ProcessFiles(string path)
        {
            var count = 0;
            try
            {
                var filelist = Directory.GetFiles(path);
                var pathdirectoriofinal = Path.Combine(path, "Archivos Convertidos");
                if (!Directory.Exists(pathdirectoriofinal))
                {
                    Directory.CreateDirectory(pathdirectoriofinal);
                }
                foreach (var file in filelist)
                {
                    var stringtransformado = ProcessFile(file);
                    var pathdestino = Path.Combine(pathdirectoriofinal, Path.GetFileName(file));
                    if (File.Exists(pathdestino))
                    {
                        File.Delete(pathdestino);
                    }
                    using (StreamWriter sw = File.CreateText(pathdestino))
                    {
                        sw.Write(stringtransformado);
                    }
                }
                count = filelist.Count();
            }
            catch (Exception e)
            {
                return new Response()
                {
                    Success = false,
                    Message = string.Format("Se ha producido un error en el proceso. Detalle: {0}.", e.Message)
                };
            }

            return new Response()
            {
                Success = true,
                Message = string.Format("Se han procesado con éxito {0} archivos en la carpeta especificada '{1}'.", count, path)
            };
        }

        public static Response RequestDirectoryPath()
        {
            Console.Write("Ingrese el path de la carpeta a procesar: ");
            var path = Console.ReadLine();
            if (Directory.Exists(path))
            {
                return new Response()
                {
                    Success = true,
                    Message = path
                };
            }
            else
            {
                return new Response()
                {
                    Success = false,
                    Message = "El path ingresado no corresponde a un directorio válido."
                };
            }
        }

        public static string ProcessFile(string path)
        {
            var contenido = File.ReadAllText(path);

            //Quitar info inicial
            var infoinicial = new Regex(@"\[.*\](\r?\n)?\r?\n");
            contenido = infoinicial.Replace(contenido, string.Empty);

            //Quita los \n del contenido original del archivo
            contenido = contenido.Replace(Environment.NewLine, " ");

            //"\{([^}]+)\}"	--> Saca los comentarios (reemplazar con nada)
            var comentarios = new Regex(@"\{([^}]+)\}");
            contenido = comentarios.Replace(contenido, string.Empty);

            //"[0-9]+\."	--> Saca los números de movimiento (reemplazar con nada)
            var numerosmov = new Regex(@"[0-9]+\.\s");
            contenido = numerosmov.Replace(contenido, string.Empty);

            numerosmov = new Regex(@"[0-9]+\.");
            contenido = numerosmov.Replace(contenido, string.Empty);

            //"  "		--> Saca los espacios dobles (reemplazar con un solo espacio)
            contenido = contenido.Replace("  ", " ");

            //" "		--> Reemplaza los espacios por un enter para separar las líneas
            contenido = contenido.Replace(" ", Environment.NewLine);

            //"^[ \t]*$\r?\n"	--> Saca las líneas en blanco (reemplazar con nada)
            var lineasblancas = new Regex(@"^[\t]*$\r?\n");
            contenido = lineasblancas.Replace(contenido, string.Empty);

            //"R"		--> Reemplaza R (Torre) por T (reemplazar con "T")
            contenido = contenido.Replace("R", "T");

            //"K"		--> Reemplaza K (Rey) por R (reemplazar con "R")
            contenido = contenido.Replace("K", "R");

            //"Q"		--> Reemplaza Q (Reina) por D (reemplazar con "D")
            contenido = contenido.Replace("Q", "D");

            //"B"		--> Reemplaza B (Alfil) por A (reemplazar con "A")
            contenido = contenido.Replace("B", "A");

            //"N"		--> Reemplaza N (Caballo) por C (reemplazar con "C")
            contenido = contenido.Replace("N", "C");

            //Quitar último salto de línea
            lineasblancas = new Regex(@"\r?\n$");
            contenido = lineasblancas.Replace(contenido, string.Empty);

            //Eliminar última línea (Resultado del match) (Puede que no haya que hacerlo)
            var resultado = contenido.Split('\n').Last();
            if (Regex.IsMatch(resultado, @"\d-\d"))
            {
                contenido = contenido.Substring(0, contenido.Length - resultado.Length);
                contenido = lineasblancas.Replace(contenido, string.Empty);
            }

            return contenido;
        }

        public static string AddSQLNotation(string path)
        {
            Console.Clear();
            Console.Write("Ingrese cod_torneo: ");
            var cod_torneo = Console.ReadLine();
            Console.Write("Ingrese nro_partida: ");
            var nro_partida = Console.ReadLine();
            Console.Write("Ingrese cod_jugador1: ");
            var jugador1 = Console.ReadLine();
            Console.Write("Ingrese cod_jugador2: ");
            var jugador2 = Console.ReadLine();

            var contenido = File.ReadLines(path);
            var contenidoSQL = string.Empty;

            var nrojugada = 1;
            var random = new Random();
            foreach (var line in contenido)
            {
                var tiempojugada = random.Next(1, 120);
                var linea = string.Format("INSERT INTO \"Jugada\"(\"Cod_torneo\", \"Nro_partida\", \"Nro_jugada\", \"Cod_jugador\", \"Tiempo\", \"Movimiento\") VALUES({0},{1},{2},{3},{4},'{5}');\n", cod_torneo, nro_partida, nrojugada++, nrojugada % 2 == 0 ? jugador1 : jugador2, tiempojugada, line);

                contenidoSQL += linea;
            };

            return contenidoSQL;
        }

        public static Response ProcessFilesSQL(string path)
        {
            var count = 0;
            try
            {
                var filelist = Directory.GetFiles(path);
                var pathdirectoriofinal = Path.Combine(path, "Archivos Convertidos SQL");
                if (!Directory.Exists(pathdirectoriofinal))
                {
                    Directory.CreateDirectory(pathdirectoriofinal);
                }
                foreach (var file in filelist)
                {
                    var stringtransformado = AddSQLNotation(file);
                    var pathdestino = Path.Combine(pathdirectoriofinal, Path.GetFileNameWithoutExtension(file) + ".sql");
                    if (File.Exists(pathdestino))
                    {
                        File.Delete(pathdestino);
                    }
                    using (StreamWriter sw = File.CreateText(pathdestino))
                    {
                        sw.Write(stringtransformado);
                    }
                }
                count = filelist.Count();
            }
            catch (Exception e)
            {
                return new Response()
                {
                    Success = false,
                    Message = string.Format("Se ha producido un error en el proceso. Detalle: {0}.", e.Message)
                };
            }

            return new Response()
            {
                Success = true,
                Message = string.Format("Se han procesado con éxito {0} archivos en la carpeta especificada '{1}'.", count, path)
            };
        }
    }
}
