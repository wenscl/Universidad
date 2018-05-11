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
            proveedor.Ciudad = txtCiudad.Text;
            proveedor.Direccion = txtDireccion.Text;
            proveedor.Telefono = Convert.ToInt32(txtTelefono.Text);
            proveedor.Mail = txtMail.Text;
            Proveedor.Agregar(proveedor);

            var frm = new ListarProveedores();
            this.Hide();
            frm.Show();
        }

        private void Cancelar_Click(object sender, EventArgs e)
        {
            txtNombre.Clear();
            txtCiudad.Clear();
            txtDireccion.Clear();
            txtTelefono.Clear();
            txtMail.Clear();

            var frm = new ListarProveedores();
            this.Hide();
            frm.Show();
        }
        
        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProductos();
            this.Hide();
            frm.Show();
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

        private void agregarProductoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProducto();
            this.Hide();
            frm.Show();
        }

        private void verPedidosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarPedidos();
            this.Hide();
            frm.Show();
        }
    }
}
