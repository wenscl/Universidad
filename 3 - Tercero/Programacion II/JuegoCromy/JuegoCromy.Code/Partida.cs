using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoCromy.Code
{
    public class Partida
    {
        public Partida(string nombre, Jugador jugador, string mazo)
        {
            if (string.IsNullOrEmpty(nombre))
            { throw new ArgumentNullException("El nombre no puede ser nulo."); }
            
            if (jugador == null)
            { throw new ArgumentNullException("No se puede crear la partida sin un jugador"); }
            
            this.Nombre = nombre;
            this.Usuario = jugador.Nombre;
            this.Mazo = mazo;
            this.Jugadores = new List<Jugador>();
            this.Jugadores.Add(jugador);
            this.ArmarMazo(mazo);

        }

        public string Nombre { get; set; }
        public string Mazo { get; set; }
        public string Usuario { get; set; }
        public Mazo MazoCartas { get; set; }
        public List<Jugador> Jugadores { get; set; }

        private string path = "G:\\Programacion II\\JuegoCromy\\JuegoCromix.Web\\Mazos";

        public void ArmarMazo(string mazo)
        {
            var x = path + "\\" + mazo + "\\" + "informacion.txt";
            string linea;
            int contador = 0;
            using (var reader = File.OpenText(x))
            {
                while (reader.ReadLine() != null) 
                { contador++; }
            }
            contador -= 2;
            var mazo1 = new Mazo(mazo, contador);
            using (var archivo = File.OpenText(x))
            {
                int i = 0;
                linea = archivo.ReadLine();

                while (linea != null)
                {
                    string [] renglon = linea.Split('|').ToArray();
                    if (i == 1)
                    {
                        for (int j = 2; j < renglon.Length; j++)
                        {
                            var tipo = (TipoAtributo)Enum.Parse(typeof(TipoAtributo), renglon[j]);
                            mazo1.Atributos.Add(tipo);
                            mazo1.NombreAtributos.Add(renglon[j]);
                        }
                    }
                    if (i > 1)
                    {
                        var carta = new Carta(renglon[1], renglon[0]);
                        var cont = 2;
                        foreach (var item in mazo1.Atributos)
                        {
                            carta.AgregarAtributo(item, Convert.ToDouble(renglon[cont]));
                            cont++;
                        }
                        mazo1.AgregarCarta(carta);
                    }
                    i++;
                    linea = archivo.ReadLine();
                }
            }
            this.MazoCartas = mazo1;
        }

        public void AgregarJugadores(Jugador NuevoJugador)
        {
            this.Jugadores.Add(NuevoJugador);
        }

        public void Repartir()
        {
            foreach (Carta c in this.MazoCartas.Cartas)
            {
                if (MazoCartas.Cartas.IndexOf(c) % 2 == 0)
                    Jugadores[0].Cartas.Add(c);         
                else
                    Jugadores[1].Cartas.Add(c);
            }
        }
    }
}
