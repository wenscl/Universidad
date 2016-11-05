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
    public partial class ListarProductos : Form
    {
        public ListarProductos()
        {
            InitializeComponent();
        }

        private void ListarProductos_Load(object sender, EventArgs e)
        {
            dataGridView1.DataSource = Producto.Listar();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Buscar_Click(object sender, EventArgs e)
        {

            //Producto.Buscar(txtBuscar.Text);
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void bindingNavigatorAddNewItem_Click(object sender, EventArgs e)
        {
            
        }

        private void Modificar_Click(object sender, EventArgs e)
        {
        }

        private void toolStripButtonAdd_Click(object sender, EventArgs e)
        {

        }

        private void toolStripButtonDelete_Click(object sender, EventArgs e)
        {
            // no anda.. 
            //Producto.Eliminar(dataGridView1.SelectedRows[0].Index);
            //dataGridView1.Refresh();
            
            foreach (DataGridViewRow item in dataGridView1.SelectedRows)
            {
                Producto.Eliminar(item.Index);
                dataGridView1.DataSource = Producto.Listar();
            }
        }

        private void BuscarProducto_Click(object sender, EventArgs e)
        {

        }

        private void agregarProductoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            AgregarProducto frm = new AgregarProducto();
            frm.Show();
        }

        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
    }
}
