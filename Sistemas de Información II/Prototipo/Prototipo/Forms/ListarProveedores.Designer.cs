namespace Prototipo.Forms
{
    partial class ListarProveedores
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ListarProveedores));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.ventasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.agregarVentaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mostrarVentasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.productosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.agregarProductoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.verProductosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.verStockToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.proveedoresToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.agregarProveedorToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mostrarProveedoresToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.realizarPedidoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reportesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mostrarReportesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.BuscarProveedor = new System.Windows.Forms.Label();
            this.txtBuscar = new System.Windows.Forms.TextBox();
            this.Limpiar = new System.Windows.Forms.Button();
            this.Agregar = new System.Windows.Forms.Button();
            this.Eliminar = new System.Windows.Forms.Button();
            this.Modificar = new System.Windows.Forms.Button();
            this.Buscar = new System.Windows.Forms.Button();
            this.seleccionarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.copiarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pegarToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.contextMenuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.ventasToolStripMenuItem,
            this.productosToolStripMenuItem,
            this.proveedoresToolStripMenuItem,
            this.reportesToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Padding = new System.Windows.Forms.Padding(7, 2, 0, 2);
            this.menuStrip1.Size = new System.Drawing.Size(1114, 24);
            this.menuStrip1.TabIndex = 21;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // ventasToolStripMenuItem
            // 
            this.ventasToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.agregarVentaToolStripMenuItem,
            this.mostrarVentasToolStripMenuItem});
            this.ventasToolStripMenuItem.Name = "ventasToolStripMenuItem";
            this.ventasToolStripMenuItem.Size = new System.Drawing.Size(53, 20);
            this.ventasToolStripMenuItem.Text = "Ventas";
            // 
            // agregarVentaToolStripMenuItem
            // 
            this.agregarVentaToolStripMenuItem.Name = "agregarVentaToolStripMenuItem";
            this.agregarVentaToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.agregarVentaToolStripMenuItem.Text = "Agregar venta";
            this.agregarVentaToolStripMenuItem.Click += new System.EventHandler(this.agregarVentaToolStripMenuItem_Click);
            // 
            // mostrarVentasToolStripMenuItem
            // 
            this.mostrarVentasToolStripMenuItem.Name = "mostrarVentasToolStripMenuItem";
            this.mostrarVentasToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.mostrarVentasToolStripMenuItem.Text = "Ver Ventas";
            this.mostrarVentasToolStripMenuItem.Click += new System.EventHandler(this.mostrarVentasToolStripMenuItem_Click);
            // 
            // productosToolStripMenuItem
            // 
            this.productosToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.agregarProductoToolStripMenuItem,
            this.verProductosToolStripMenuItem,
            this.verStockToolStripMenuItem});
            this.productosToolStripMenuItem.Name = "productosToolStripMenuItem";
            this.productosToolStripMenuItem.Size = new System.Drawing.Size(73, 20);
            this.productosToolStripMenuItem.Text = "Productos";
            // 
            // agregarProductoToolStripMenuItem
            // 
            this.agregarProductoToolStripMenuItem.Name = "agregarProductoToolStripMenuItem";
            this.agregarProductoToolStripMenuItem.Size = new System.Drawing.Size(168, 22);
            this.agregarProductoToolStripMenuItem.Text = "Agregar producto";
            this.agregarProductoToolStripMenuItem.Click += new System.EventHandler(this.agregarProductoToolStripMenuItem_Click);
            // 
            // verProductosToolStripMenuItem
            // 
            this.verProductosToolStripMenuItem.Name = "verProductosToolStripMenuItem";
            this.verProductosToolStripMenuItem.Size = new System.Drawing.Size(168, 22);
            this.verProductosToolStripMenuItem.Text = "Ver productos";
            this.verProductosToolStripMenuItem.Click += new System.EventHandler(this.verProductosToolStripMenuItem_Click);
            // 
            // verStockToolStripMenuItem
            // 
            this.verStockToolStripMenuItem.Name = "verStockToolStripMenuItem";
            this.verStockToolStripMenuItem.Size = new System.Drawing.Size(168, 22);
            this.verStockToolStripMenuItem.Text = "Ver stock";
            // 
            // proveedoresToolStripMenuItem
            // 
            this.proveedoresToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.agregarProveedorToolStripMenuItem,
            this.mostrarProveedoresToolStripMenuItem,
            this.realizarPedidoToolStripMenuItem});
            this.proveedoresToolStripMenuItem.Name = "proveedoresToolStripMenuItem";
            this.proveedoresToolStripMenuItem.Size = new System.Drawing.Size(84, 20);
            this.proveedoresToolStripMenuItem.Text = "Proveedores";
            // 
            // agregarProveedorToolStripMenuItem
            // 
            this.agregarProveedorToolStripMenuItem.Name = "agregarProveedorToolStripMenuItem";
            this.agregarProveedorToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.agregarProveedorToolStripMenuItem.Text = "Agregar proveedor";
            this.agregarProveedorToolStripMenuItem.Click += new System.EventHandler(this.agregarProveedorToolStripMenuItem_Click);
            // 
            // mostrarProveedoresToolStripMenuItem
            // 
            this.mostrarProveedoresToolStripMenuItem.Name = "mostrarProveedoresToolStripMenuItem";
            this.mostrarProveedoresToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.mostrarProveedoresToolStripMenuItem.Text = "Ver proveedores";
            // 
            // realizarPedidoToolStripMenuItem
            // 
            this.realizarPedidoToolStripMenuItem.Name = "realizarPedidoToolStripMenuItem";
            this.realizarPedidoToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.realizarPedidoToolStripMenuItem.Text = "Realizar pedido";
            this.realizarPedidoToolStripMenuItem.Click += new System.EventHandler(this.realizarPedidoToolStripMenuItem_Click);
            // 
            // reportesToolStripMenuItem
            // 
            this.reportesToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mostrarReportesToolStripMenuItem});
            this.reportesToolStripMenuItem.Name = "reportesToolStripMenuItem";
            this.reportesToolStripMenuItem.Size = new System.Drawing.Size(65, 20);
            this.reportesToolStripMenuItem.Text = "Reportes";
            // 
            // mostrarReportesToolStripMenuItem
            // 
            this.mostrarReportesToolStripMenuItem.Name = "mostrarReportesToolStripMenuItem";
            this.mostrarReportesToolStripMenuItem.Size = new System.Drawing.Size(161, 22);
            this.mostrarReportesToolStripMenuItem.Text = "Mostrar reportes";
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.seleccionarToolStripMenuItem,
            this.copiarToolStripMenuItem,
            this.pegarToolStripMenuItem});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(135, 70);
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToAddRows = false;
            this.dataGridView1.AllowUserToDeleteRows = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.GridColor = System.Drawing.Color.Black;
            this.dataGridView1.Location = new System.Drawing.Point(12, 97);
            this.dataGridView1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.ReadOnly = true;
            this.dataGridView1.Size = new System.Drawing.Size(1067, 341);
            this.dataGridView1.TabIndex = 28;
            // 
            // BuscarProveedor
            // 
            this.BuscarProveedor.AutoSize = true;
            this.BuscarProveedor.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.BuscarProveedor.Location = new System.Drawing.Point(206, 44);
            this.BuscarProveedor.Name = "BuscarProveedor";
            this.BuscarProveedor.Size = new System.Drawing.Size(128, 19);
            this.BuscarProveedor.TabIndex = 26;
            this.BuscarProveedor.Text = "Buscar Proveedor";
            // 
            // txtBuscar
            // 
            this.txtBuscar.Location = new System.Drawing.Point(340, 43);
            this.txtBuscar.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtBuscar.Name = "txtBuscar";
            this.txtBuscar.Size = new System.Drawing.Size(290, 20);
            this.txtBuscar.TabIndex = 25;
            // 
            // Limpiar
            // 
            this.Limpiar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Limpiar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Limpiar.Image = global::Prototipo.Properties.Resources._1478491184_broom_stick_3;
            this.Limpiar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Limpiar.Location = new System.Drawing.Point(781, 34);
            this.Limpiar.Name = "Limpiar";
            this.Limpiar.Size = new System.Drawing.Size(97, 37);
            this.Limpiar.TabIndex = 32;
            this.Limpiar.Text = "Limpiar";
            this.Limpiar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Limpiar.UseVisualStyleBackColor = true;
            this.Limpiar.Click += new System.EventHandler(this.Limpiar_Click);
            // 
            // Agregar
            // 
            this.Agregar.FlatAppearance.BorderSize = 2;
            this.Agregar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Agregar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Agregar.Image = global::Prototipo.Properties.Resources.save;
            this.Agregar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Agregar.Location = new System.Drawing.Point(465, 468);
            this.Agregar.Name = "Agregar";
            this.Agregar.Size = new System.Drawing.Size(108, 37);
            this.Agregar.TabIndex = 31;
            this.Agregar.Text = "Agregar";
            this.Agregar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Agregar.UseVisualStyleBackColor = true;
            this.Agregar.Click += new System.EventHandler(this.Agregar_Click);
            // 
            // Eliminar
            // 
            this.Eliminar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Eliminar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Eliminar.Image = global::Prototipo.Properties.Resources.delete;
            this.Eliminar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Eliminar.Location = new System.Drawing.Point(728, 468);
            this.Eliminar.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Eliminar.Name = "Eliminar";
            this.Eliminar.Size = new System.Drawing.Size(103, 37);
            this.Eliminar.TabIndex = 30;
            this.Eliminar.Text = "Eliminar";
            this.Eliminar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Eliminar.UseVisualStyleBackColor = true;
            this.Eliminar.Click += new System.EventHandler(this.Eliminar_Click);
            // 
            // Modificar
            // 
            this.Modificar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Modificar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Modificar.Image = global::Prototipo.Properties.Resources.edit;
            this.Modificar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Modificar.Location = new System.Drawing.Point(594, 468);
            this.Modificar.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Modificar.Name = "Modificar";
            this.Modificar.Size = new System.Drawing.Size(113, 37);
            this.Modificar.TabIndex = 29;
            this.Modificar.Text = "Modificar";
            this.Modificar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Modificar.UseVisualStyleBackColor = true;
            this.Modificar.Click += new System.EventHandler(this.Modificar_Click);
            // 
            // Buscar
            // 
            this.Buscar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Buscar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Buscar.Image = global::Prototipo.Properties.Resources._1478490982_search;
            this.Buscar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Buscar.Location = new System.Drawing.Point(651, 34);
            this.Buscar.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Buscar.Name = "Buscar";
            this.Buscar.Size = new System.Drawing.Size(101, 37);
            this.Buscar.TabIndex = 27;
            this.Buscar.Text = "Buscar";
            this.Buscar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Buscar.UseVisualStyleBackColor = true;
            this.Buscar.Click += new System.EventHandler(this.Buscar_Click);
            // 
            // seleccionarToolStripMenuItem
            // 
            this.seleccionarToolStripMenuItem.Image = ((System.Drawing.Image)(resources.GetObject("seleccionarToolStripMenuItem.Image")));
            this.seleccionarToolStripMenuItem.Name = "seleccionarToolStripMenuItem";
            this.seleccionarToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.seleccionarToolStripMenuItem.Text = "Seleccionar";
            // 
            // copiarToolStripMenuItem
            // 
            this.copiarToolStripMenuItem.Image = ((System.Drawing.Image)(resources.GetObject("copiarToolStripMenuItem.Image")));
            this.copiarToolStripMenuItem.Name = "copiarToolStripMenuItem";
            this.copiarToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.copiarToolStripMenuItem.Text = "Copiar";
            // 
            // pegarToolStripMenuItem
            // 
            this.pegarToolStripMenuItem.Image = global::Prototipo.Properties.Resources.paste;
            this.pegarToolStripMenuItem.Name = "pegarToolStripMenuItem";
            this.pegarToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.pegarToolStripMenuItem.Text = "Pegar";
            // 
            // ListarProveedores
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1114, 550);
            this.Controls.Add(this.Limpiar);
            this.Controls.Add(this.Agregar);
            this.Controls.Add(this.Eliminar);
            this.Controls.Add(this.Modificar);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.Buscar);
            this.Controls.Add(this.BuscarProveedor);
            this.Controls.Add(this.txtBuscar);
            this.Controls.Add(this.menuStrip1);
            this.Name = "ListarProveedores";
            this.Text = "ListarProveedores";
            this.Load += new System.EventHandler(this.ListarProveedores_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.contextMenuStrip1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem ventasToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem agregarVentaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mostrarVentasToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem productosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem agregarProductoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem verProductosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem verStockToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem proveedoresToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem agregarProveedorToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mostrarProveedoresToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem realizarPedidoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reportesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mostrarReportesToolStripMenuItem;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem seleccionarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem copiarToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem pegarToolStripMenuItem;
        private System.Windows.Forms.Button Limpiar;
        private System.Windows.Forms.Button Agregar;
        private System.Windows.Forms.Button Eliminar;
        private System.Windows.Forms.Button Modificar;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Button Buscar;
        private System.Windows.Forms.Label BuscarProveedor;
        private System.Windows.Forms.TextBox txtBuscar;
    }
}