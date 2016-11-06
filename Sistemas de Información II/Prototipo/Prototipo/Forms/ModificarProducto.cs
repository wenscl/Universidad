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
    public partial class ModificarProducto : Form
    {
        public ModificarProducto()
        {
            InitializeComponent();
        }

        public int Id { get; set; }

        public ModificarProducto(int id, string codigo, string nombre, string tipo, string marca, string precio, string stock)
        {
            InitializeComponent();
            Id = id;
            txtCodigo.Text = codigo;
            txtNombre.Text = nombre;
            txtTipo.Text = tipo;
            txtMarca.Text = marca;
            txtStock.Text = stock;
            txtPrecio.Text = precio;
        }

        private void Agregar_Click(object sender, EventArgs e)
        {
            var producto = new Producto();
            producto.Id = Id;
            producto.Codigo = txtCodigo.Text;
            producto.Nombre = txtNombre.Text;
            producto.Tipo = txtTipo.Text;
            producto.Marca = txtMarca.Text;
            producto.Precio = Convert.ToSingle(txtPrecio.Text);
            producto.Stock = Convert.ToInt32(txtStock.Text);
            Producto.Modificar(producto);

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
        }

        private void agregarProductoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProducto();
            this.Hide();
            frm.Show();
        }

        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProductos();
            this.Hide();
            frm.Show();
        }

        private void verStockToolStripMenuItem_Click(object sender, EventArgs e)
        {

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

        private void mostrarReportesToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void ModificarProducto_Load(object sender, EventArgs e)
        {
        }
    }
}
