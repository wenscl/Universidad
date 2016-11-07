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
    public class DetalleVenta
    {
        public int Id { get; set; }
        public int IdVenta { get; set; }
        public string CodigoProducto { get; set; }
        public int Cantidad { get; set; }
        public float Precio { get; set; }

        public static string BD = Path.Combine(System.IO.Path.GetDirectoryName(Application.ExecutablePath), "BDPrototipo.db");

        public static void Agregar(DetalleVenta detalle)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVenta");

                detalles.Insert(detalle);
            }
        }

        // Detalle ventas
        public static IEnumerable<DetalleVenta> Listar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVenta");

                return detalles.Find(x => x.IdVenta == id);
            }
        }

        // Eliminar detalle
        public static void Eliminar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVenta");

                detalles.Delete(id);
            }
        }

        public static List<DetalleVenta> Todos()
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVenta");

                return detalles.FindAll().ToList();
            }
        }

        public static void EliminarTabla()
        {
            using (var db = new LiteDatabase(BD))
            {
                db.DropCollection("DetalleVenta");
            }
        }
    }
}
