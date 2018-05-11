using Prototipo.Class;
using Prototipo.Forms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prototipo
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            //DetalleVenta.EliminarTabla();
            //Venta.EliminarTabla();
            //Producto.EliminarTabla();
            //Pedido.EliminarTabla();
            //DetallePedido.EliminarTabla();
            //Proveedor.EliminarTabla();
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new AgregarVenta());
        }
    }
}
