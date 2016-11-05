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
        
        private void Agregar_Click(object sender, EventArgs e)
        {
            var producto = new Producto();
            producto.Codigo = txtCodigo.Text;
            producto.Nombre = txtNombre.Text;
            producto.Tipo = txtTipo.Text;
            producto.Marca = txtMarca.Text;
            producto.Precio = Convert.ToSingle(txtPrecio.Text);
            producto.Stock = Convert.ToInt32(txtStock.Text);
            Producto.Modificar(producto);
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
            AgregarProducto frm = new AgregarProducto();
            frm.Show();
        }

        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ListarProductos frm = new ListarProductos();
            frm.Show();
        }
    }
}
