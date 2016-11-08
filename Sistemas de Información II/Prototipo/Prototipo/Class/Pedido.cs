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
    public class Pedido
    {
        public int Id { get; set; }
        public string Proveedor { get; set; }
        public DateTime Fecha { get; set; }

        //Funciones
        public static string BD = Path.Combine(System.IO.Path.GetDirectoryName(Application.ExecutablePath), "BDPrototipo.db");

        // Agregar pedido
        public static void Agregar(Pedido pedido)
        {
            using (var db = new LiteDatabase(BD))
            {
                var pedidos = db.GetCollection<Pedido>("Pedidos");

                pedidos.Insert(pedido);
            }
        }

        // Modificar pedidos
        public static void Modificar(Pedido pedido)
        {
            using (var db = new LiteDatabase(BD))
            {
                var pedidos = db.GetCollection<Pedido>("Pedidos");

                pedidos.Update(pedido);
            }
        }

        // Eliminar pedidos
        public static void Eliminar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var pedidos = db.GetCollection<Pedido>("Pedidos");

                pedidos.Delete(id);
            }
        }

        // Listar pedidos
        public static List<Pedido> Listar()
        {
            using (var db = new LiteDatabase(BD))
            {
                var pedidos = db.GetCollection<Pedido>("Pedidos");

                return pedidos.FindAll().ToList();
            }
        }

        // Buscar pedidos
        public static Pedido Buscar(int id)
        {
            using (var db = new LiteDatabase(BD))
            {
                var pedidos = db.GetCollection<Pedido>("Pedidos");

                return pedidos.FindById(id);
            }
        }

        public static void EliminarTabla()
        {
            using (var db = new LiteDatabase(BD))
            {
                db.DropCollection("Pedidos");
            }
        }
    }
}
