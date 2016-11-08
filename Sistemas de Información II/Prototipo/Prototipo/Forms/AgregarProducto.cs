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
    public partial class AgregarProducto : Form
    {
        public AgregarProducto()
        {
            InitializeComponent();
        }

        private void Agregar_Click(object sender, EventArgs e)
        {
            var producto = new Producto();
            producto.Codigo = txtCodigo.Text;
            producto.Nombre = txtNombre.Text;
            producto.Tipo = txtTipo.Text;
            producto.Marca = txtMarca.Text;
            producto.Precio = Convert.ToSingle(txtPrecio.Text);
            producto.Stock = Convert.ToInt32(txtStock.Text);
            Producto.Agregar(producto);

            var frm = new ListarProductos();
            this.Hide();
            frm.Show();
        }

        private void Cancelar_Click(object sender, EventArgs e)
        {
            txtCodigo.Clear();
            txtNombre.Clear();
            txtTipo.Clear();
            txtMarca.Clear();
            txtPrecio.Clear();
            txtStock.Clear();

            var frm = new ListarProductos();
            this.Hide();
            frm.Show();
        }
        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProductos();
            this.Hide();
            frm.Show();
        }
        
        private void agregarProveedorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProveedor();
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

        private void verPedidosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarPedidos();
            this.Hide();
            frm.Show();
        }
    }
}
