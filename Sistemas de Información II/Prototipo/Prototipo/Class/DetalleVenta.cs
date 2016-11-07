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
                var detalles = db.GetCollection<DetalleVenta>("DetalleVentas");

                detalles.Insert(detalle);
            }
        }

        // Detalle ventas
        public static List<DetalleVenta> Listar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVentas");

                return detalles.Find(Query.EQ("IdVenta", id)).ToList();
            }
        }

        // Eliminar detalle
        public static void Eliminar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVentas");

                detalles.Delete(id);
            }
        }

        public static List<DetalleVenta> Todos()
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVentas");

                return detalles.FindAll().ToList();
            }
        }

        public static void EliminarTabla()
        {
            using (var db = new LiteDatabase(BD))
            {
                db.DropCollection("DetalleVentas");
            }
        }

        public static List<DetalleVenta> EliminarDetalle(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetalleVenta>("DetalleVentas");

                return detalles.Find(x => x.IdVenta == id).ToList();
            }
        }
    }
}
