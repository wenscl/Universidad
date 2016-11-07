namespace Prototipo.Forms
{
    partial class AgregarVenta
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
            this.dataGridVentas = new System.Windows.Forms.DataGridView();
            this.Agregar = new System.Windows.Forms.Button();
            this.Eliminar = new System.Windows.Forms.Button();
            this.Modificar = new System.Windows.Forms.Button();
            this.dataGridDetalle = new System.Windows.Forms.DataGridView();
            this.Terminar = new System.Windows.Forms.Button();
            this.txtProducto = new System.Windows.Forms.TextBox();
            this.txtCantidad = new System.Windows.Forms.TextBox();
            this.BuscarProducto = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.Siguiente = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.txtPrecio = new System.Windows.Forms.TextBox();
            this.VerDetalle = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridVentas)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridDetalle)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridVentas
            // 
            this.dataGridVentas.AllowUserToAddRows = false;
            this.dataGridVentas.AllowUserToDeleteRows = false;
            this.dataGridVentas.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridVentas.Location = new System.Drawing.Point(12, 27);
            this.dataGridVentas.Name = "dataGridVentas";
            this.dataGridVentas.ReadOnly = true;
            this.dataGridVentas.Size = new System.Drawing.Size(388, 366);
            this.dataGridVentas.TabIndex = 0;
            // 
            // Agregar
            // 
            this.Agregar.FlatAppearance.BorderSize = 2;
            this.Agregar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Agregar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Agregar.Image = global::Prototipo.Properties.Resources.add;
            this.Agregar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Agregar.Location = new System.Drawing.Point(34, 438);
            this.Agregar.Name = "Agregar";
            this.Agregar.Size = new System.Drawing.Size(102, 37);
            this.Agregar.TabIndex = 26;
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
            this.Eliminar.Location = new System.Drawing.Point(297, 438);
            this.Eliminar.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Eliminar.Name = "Eliminar";
            this.Eliminar.Size = new System.Drawing.Size(103, 37);
            this.Eliminar.TabIndex = 25;
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
            this.Modificar.Location = new System.Drawing.Point(163, 438);
            this.Modificar.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Modificar.Name = "Modificar";
            this.Modificar.Size = new System.Drawing.Size(113, 37);
            this.Modificar.TabIndex = 24;
            this.Modificar.Text = "Modificar";
            this.Modificar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Modificar.UseVisualStyleBackColor = true;
            this.Modificar.Click += new System.EventHandler(this.Modificar_Click);
            // 
            // dataGridDetalle
            // 
            this.dataGridDetalle.AllowUserToAddRows = false;
            this.dataGridDetalle.AllowUserToDeleteRows = false;
            this.dataGridDetalle.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridDetalle.Location = new System.Drawing.Point(422, 190);
            this.dataGridDetalle.Name = "dataGridDetalle";
            this.dataGridDetalle.ReadOnly = true;
            this.dataGridDetalle.Size = new System.Drawing.Size(476, 203);
            this.dataGridDetalle.TabIndex = 27;
            // 
            // Terminar
            // 
            this.Terminar.Enabled = false;
            this.Terminar.FlatAppearance.BorderSize = 2;
            this.Terminar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Terminar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Terminar.Image = global::Prototipo.Properties.Resources.save;
            this.Terminar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Terminar.Location = new System.Drawing.Point(735, 96);
            this.Terminar.Name = "Terminar";
            this.Terminar.Size = new System.Drawing.Size(108, 37);
            this.Terminar.TabIndex = 28;
            this.Terminar.Text = "Terminar";
            this.Terminar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Terminar.UseVisualStyleBackColor = true;
            this.Terminar.Click += new System.EventHandler(this.Terminar_Click);
            // 
            // txtProducto
            // 
            this.txtProducto.Enabled = false;
            this.txtProducto.Location = new System.Drawing.Point(554, 24);
            this.txtProducto.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtProducto.Name = "txtProducto";
            this.txtProducto.Size = new System.Drawing.Size(93, 20);
            this.txtProducto.TabIndex = 29;
            // 
            // txtCantidad
            // 
            this.txtCantidad.Enabled = false;
            this.txtCantidad.Location = new System.Drawing.Point(554, 72);
            this.txtCantidad.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtCantidad.Name = "txtCantidad";
            this.txtCantidad.Size = new System.Drawing.Size(93, 20);
            this.txtCantidad.TabIndex = 31;
            // 
            // BuscarProducto
            // 
            this.BuscarProducto.AutoSize = true;
            this.BuscarProducto.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.BuscarProducto.Location = new System.Drawing.Point(418, 27);
            this.BuscarProducto.Name = "BuscarProducto";
            this.BuscarProducto.Size = new System.Drawing.Size(72, 19);
            this.BuscarProducto.TabIndex = 30;
            this.BuscarProducto.Text = "Producto";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(418, 73);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(77, 19);
            this.label1.TabIndex = 33;
            this.label1.Text = "Cantidad";
            // 
            // Siguiente
            // 
            this.Siguiente.Enabled = false;
            this.Siguiente.FlatAppearance.BorderSize = 2;
            this.Siguiente.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Siguiente.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Siguiente.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Siguiente.Location = new System.Drawing.Point(735, 27);
            this.Siguiente.Name = "Siguiente";
            this.Siguiente.Size = new System.Drawing.Size(86, 37);
            this.Siguiente.TabIndex = 34;
            this.Siguiente.Text = "Siguiente";
            this.Siguiente.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Siguiente.UseVisualStyleBackColor = true;
            this.Siguiente.Click += new System.EventHandler(this.Siguiente_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(418, 114);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(51, 19);
            this.label2.TabIndex = 36;
            this.label2.Text = "Precio";
            // 
            // txtPrecio
            // 
            this.txtPrecio.Enabled = false;
            this.txtPrecio.Location = new System.Drawing.Point(554, 113);
            this.txtPrecio.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtPrecio.Name = "txtPrecio";
            this.txtPrecio.Size = new System.Drawing.Size(93, 20);
            this.txtPrecio.TabIndex = 35;
            // 
            // VerDetalle
            // 
            this.VerDetalle.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.VerDetalle.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.VerDetalle.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.VerDetalle.Location = new System.Drawing.Point(422, 438);
            this.VerDetalle.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.VerDetalle.Name = "VerDetalle";
            this.VerDetalle.Size = new System.Drawing.Size(94, 37);
            this.VerDetalle.TabIndex = 37;
            this.VerDetalle.Text = "Ver Detalle";
            this.VerDetalle.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.VerDetalle.UseVisualStyleBackColor = true;
            this.VerDetalle.Click += new System.EventHandler(this.VerDetalle_Click);
            // 
            // AgregarVenta
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1025, 487);
            this.Controls.Add(this.VerDetalle);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtPrecio);
            this.Controls.Add(this.Siguiente);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtCantidad);
            this.Controls.Add(this.BuscarProducto);
            this.Controls.Add(this.txtProducto);
            this.Controls.Add(this.Terminar);
            this.Controls.Add(this.dataGridDetalle);
            this.Controls.Add(this.Agregar);
            this.Controls.Add(this.Eliminar);
            this.Controls.Add(this.Modificar);
            this.Controls.Add(this.dataGridVentas);
            this.Name = "AgregarVenta";
            this.Text = "AgregarVenta";
            this.Load += new System.EventHandler(this.AgregarVenta_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridVentas)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridDetalle)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridVentas;
        private System.Windows.Forms.Button Agregar;
        private System.Windows.Forms.Button Eliminar;
        private System.Windows.Forms.Button Modificar;
        private System.Windows.Forms.DataGridView dataGridDetalle;
        private System.Windows.Forms.Button Terminar;
        private System.Windows.Forms.TextBox txtProducto;
        private System.Windows.Forms.TextBox txtCantidad;
        private System.Windows.Forms.Label BuscarProducto;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button Siguiente;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtPrecio;
        private System.Windows.Forms.Button VerDetalle;
    }
}