using Prototipo.Class;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prototipo.Forms
{
    public partial class AgregarProveedor : Form
    {
        public AgregarProveedor()
        {
            InitializeComponent();
        }
        private void Agregar_Click(object sender, EventArgs e)
        {
            var proveedor = new Proveedor();
            proveedor.Nombre = txtNombre.Text;
            proveedor.Direccion = txtDireccion.Text;
            proveedor.Telefono = Convert.ToInt32(txtTelefono.Text);
            proveedor.Mail = txtMail.Text;
            proveedor.Ciudad = txtCiudad.Text;
            Proveedor.Agregar(proveedor);

            var frm = new ListarProveedores();
            this.Hide();
            frm.Show();
        }

        private void Cancelar_Click(object sender, EventArgs e)
        {
            txtNombre.Clear();
            txtDireccion.Clear();
            txtTelefono.Clear();
            txtMail.Clear();
            txtCiudad.Clear();

            var frm = new ListarProveedores();
            this.Hide();
            frm.Show();
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void agregarProductoToolStripMenuItem_Click(object sender, EventArgs e)
        {
        }

        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProductos();
            this.Hide();
            frm.Show();
        }

        private void contextMenuStrip1_Opening(object sender, CancelEventArgs e)
        {

        }

        private void agregarProveedorToolStripMenuItem_Click(object sender, EventArgs e)
        {
        }

        private void mostrarProveedoresToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProveedores();
            this.Hide();
            frm.Show();
        }

        private void realizarPedidoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarPedido();
            this.Hide();
            frm.Show();
        }

        private void agregarVentaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarVenta();
            this.Hide();
            frm.Show();
        }

        private void mostrarVentasToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarVentas();
            this.Hide();
            frm.Show();
        }

        private void verStockToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void mostrarReportesToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
        
    }
}
