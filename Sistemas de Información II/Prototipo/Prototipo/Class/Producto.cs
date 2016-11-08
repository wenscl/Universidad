using LiteDB;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prototipo.Class
{
    public class Producto
    {
        // Atributos

        public int Id { get; set; }
        public string Codigo { get; set; }
        public string Nombre { get; set; }
        public string Tipo { get; set; }
        public string Marca { get; set; }
        public float Precio { get; set; }
        public int Stock { get; set; }

        public static string BD = Path.Combine(System.IO.Path.GetDirectoryName(Application.ExecutablePath), "BDPrototipo.db");

        // Funciones

        // Agregar producto
        public static void Agregar(Producto producto)
        {
            using (var db = new LiteDatabase(BD))
            {
                var productos = db.GetCollection<Producto>("Productos");

                productos.Insert(producto);
            }
        }

        // Modificar productos
        public static void Modificar(Producto producto)
        {
            using (var db = new LiteDatabase(BD))
            {
                var productos = db.GetCollection<Producto>("Productos");

                productos.Update(producto);
            }
        }

        // Eliminar productos
        public static void Eliminar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var productos = db.GetCollection<Producto>("Productos");

                productos.Delete(id);
            }
        }

        // Listar productos
        public static List<Producto> Listar()
        {
            using (var db = new LiteDatabase(BD))
            {
                var productos = db.GetCollection<Producto>("Productos");

                return productos.FindAll().ToList();
            }
        }

        // Buscar producto
        public static List<Producto> Buscar(string nombre)
        {
            using (var db = new LiteDatabase(BD))
            {
                var productos = db.GetCollection<Producto>("Productos");

                return productos.Find(Query.Contains("Nombre", nombre)).ToList();
            }
        }

        public static List<string> Listar2()
        {
            using (var db = new LiteDatabase(BD))
            {
                var productos = db.GetCollection<Producto>("Productos");

                return productos.Find(Query.All()).Select(x => x.Codigo).ToList();
            }
        }

        public static void EliminarTabla()
        {
            using (var db = new LiteDatabase(BD))
            {
                db.DropCollection("Productos");
            }
        }
    }
}
