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
    public class Venta
    {
        public int Id { get; set; }
        public DateTime Fecha { get; set; }
        public float Total { get; set; }

        public static string BD = Path.Combine(System.IO.Path.GetDirectoryName(Application.ExecutablePath), "BDPrototipo.db");

        public static void Agregar(Venta venta)
        {
            using (var db = new LiteDatabase(BD))
            {
                var ventas = db.GetCollection<Venta>("Ventas");

                ventas.Insert(venta);
            }
        }

        // Modificar ventas
        public static void Modificar(Venta venta)
        {
            using (var db = new LiteDatabase(BD))
            {
                var ventas = db.GetCollection<Venta>("Ventas");

                ventas.Update(venta);
            }
        }

        // Eliminar ventas
        public static void Eliminar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var ventas = db.GetCollection<Venta>("Ventas");

                ventas.Delete(id);
            }
        }

        // Listar ventas
        public static List<Venta> Listar()
        {
            using (var db = new LiteDatabase(BD))
            {
                var ventas = db.GetCollection<Venta>("Ventas");

                return ventas.FindAll().ToList();
            }
        }

        // Buscar venta
        //public static Venta Buscar(int id)
        //{
        //    using (var db = new LiteDatabase(BD))
        //    {
        //        var ventas = db.GetCollection<Venta>("Ventas");

        //        return ventas.FindById(id);
        //    }
        //}

        public static void EliminarTabla()
        {
            using (var db = new LiteDatabase(BD))
            {
                db.DropCollection("Ventas");
            }
        }
    }
}
