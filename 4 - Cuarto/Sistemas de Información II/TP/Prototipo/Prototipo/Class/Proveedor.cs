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
    public class Proveedor
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public string Ciudad { get; set; }
        public string Direccion { get; set; }
        public int Telefono { get; set; }
        public string Mail { get; set; }

        //Funciones
        public static string BD = Path.Combine(System.IO.Path.GetDirectoryName(Application.ExecutablePath), "BDPrototipo.db");

        // Agregar proveedor
        public static void Agregar(Proveedor proveedor)
        {
            using (var db = new LiteDatabase(BD))
            {
                var proveedores = db.GetCollection<Proveedor>("Proveedor");

                proveedores.Insert(proveedor);
            }
        }

        // Modificar proveedores
        public static void Modificar(Proveedor proveedor)
        {
            using (var db = new LiteDatabase(BD))
            {
                var proveedores = db.GetCollection<Proveedor>("Proveedor");

                proveedores.Update(proveedor);
            }
        }

        // Eliminar proveedores
        public static void Eliminar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var proveedores = db.GetCollection<Proveedor>("Proveedor");

                proveedores.Delete(id);
            }
        }

        // Listar proveedores
        public static List<Proveedor> Listar()
        {
            using (var db = new LiteDatabase(BD))
            {
                var proveedores = db.GetCollection<Proveedor>("Proveedor");

                return proveedores.FindAll().ToList();
            }
        }

        // Buscar proveedores
        public static IEnumerable<Proveedor> Buscar(string nombre)
        {
            using (var db = new LiteDatabase(BD))
            {
                var proveedores = db.GetCollection<Proveedor>("Proveedor");

                return proveedores.Find(Query.Contains("Nombre", nombre));
            }
        }

        public static List<string> Listar2()
        {
            using (var db = new LiteDatabase(BD))
            {
                var proveedores = db.GetCollection<Proveedor>("Proveedor");

                return proveedores.Find(Query.All()).Select(x => x.Nombre).ToList();
            }
        }

        public static void EliminarTabla()
        {
            using (var db = new LiteDatabase(BD))
            {
                db.DropCollection("Proveedor");
            }
        }
    }
}
