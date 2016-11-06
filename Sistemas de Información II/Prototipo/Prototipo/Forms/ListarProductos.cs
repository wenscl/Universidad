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
            dataGridView1.DataSource = Producto.Buscar(txtBuscar.Text).ToList();
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
        }

        private void BuscarProducto_Click(object sender, EventArgs e)
        {

        }

        private void agregarProductoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProducto();
            this.Hide();
            frm.Show();
        }

        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void Modificar_Click_1(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(dataGridView1.SelectedRows[0].Cells["Id"].Value);
                var codigo = dataGridView1.SelectedRows[0].Cells["Codigo"].Value.ToString();
                var nombre = dataGridView1.SelectedRows[0].Cells["Nombre"].Value.ToString();
                var tipo = dataGridView1.SelectedRows[0].Cells["Tipo"].Value.ToString();
                var marca = dataGridView1.SelectedRows[0].Cells["Marca"].Value.ToString();
                var precio = dataGridView1.SelectedRows[0].Cells["Precio"].Value.ToString();
                var stock = dataGridView1.SelectedRows[0].Cells["Stock"].Value.ToString();

                var frm = new ModificarProducto(id, codigo, nombre, tipo, marca, precio, stock);
                this.Hide();
                frm.Show();
            }
        }

        private void Eliminar_Click(object sender, EventArgs e)
        {
            var id = dataGridView1.SelectedRows[0].Cells["Id"].Value.ToString();
            Producto.Eliminar(Convert.ToInt32(id));
            dataGridView1.Refresh();
        }

        private void Agregar_Click(object sender, EventArgs e)
        {
        }

        private void Agregar_Click_1(object sender, EventArgs e)
        {
            var frm = new AgregarProducto();
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

        private void Limpiar_Click(object sender, EventArgs e)
        {
            dataGridView1.DataSource = Producto.Listar();
        }
    }
}
