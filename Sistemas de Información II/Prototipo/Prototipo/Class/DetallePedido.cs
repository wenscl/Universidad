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
    public class DetallePedido
    {
        public int Id { get; set; }
        public int IdPedido { get; set; }
        public string Producto { get; set; }
        public int Cantidad { get; set; }

        public static string BD = Path.Combine(System.IO.Path.GetDirectoryName(Application.ExecutablePath), "BDPrototipo.db");
        
        // Agregar detalle
        public static void Agregar(DetallePedido detalle)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetallePedido>("DetallePedidos");
                detalles.Insert(detalle);
            }
        }

        // Modificar ventas
        public static void Modificar(DetallePedido detalle)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetallePedido>("DetallePedidos");

                detalles.Update(detalle);
            }
        }

        // Detalle ventas
        public static List<DetallePedido> Listar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetallePedido>("DetallePedidos");

                return detalles.Find(Query.EQ("IdPedido", id)).ToList();
            }
        }

        // Eliminar detalle
        public static void Eliminar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetallePedido>("DetallePedidos");

                detalles.Delete(id);
            }
        }

        public static List<DetallePedido> Todos()
        {
            using (var db = new LiteDatabase(BD))
            {
                var detalles = db.GetCollection<DetallePedido>("DetallePedidos");

                return detalles.FindAll().ToList();
            }
        }

        public static void EliminarTabla()
        {
            using (var db = new LiteDatabase(BD))
            {
                db.DropCollection("DetallePedidos");
            }
        }
    }
}
