object frmEjercicio3: TfrmEjercicio3
  Left = 233
  Top = 122
  Width = 1030
  Height = 563
  Caption = 'frmEjercicio3'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  Menu = MainMenu1
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object GroupBox3: TGroupBox
    Left = 32
    Top = 72
    Width = 561
    Height = 105
    Caption = '1'
    TabOrder = 3
    object Label2: TLabel
      Left = 384
      Top = 36
      Width = 99
      Height = 13
      Caption = 'Cantidad de registros'
    end
    object Label1: TLabel
      Left = 144
      Top = 28
      Width = 70
      Height = 13
      Caption = 'Valor numerico'
    end
    object Destino: TRadioButton
      Left = 16
      Top = 24
      Width = 113
      Height = 17
      Caption = 'Destino'
      TabOrder = 0
    end
    object Estado: TRadioButton
      Left = 16
      Top = 48
      Width = 113
      Height = 17
      Caption = 'Estado'
      TabOrder = 1
    end
    object CantidadDormitoris: TRadioButton
      Left = 16
      Top = 72
      Width = 129
      Height = 17
      Caption = 'CantidadDormitoris'
      TabOrder = 2
    end
    object edtValor: TEdit
      Left = 144
      Top = 44
      Width = 121
      Height = 21
      TabOrder = 3
      Text = 'edtValor'
    end
    object Filtrar: TButton
      Left = 280
      Top = 16
      Width = 81
      Height = 33
      Caption = 'Filtrar'
      TabOrder = 4
      OnClick = FiltrarClick
    end
    object Cancelar: TButton
      Left = 280
      Top = 56
      Width = 81
      Height = 33
      Caption = 'Cancelar'
      TabOrder = 5
      OnClick = CancelarClick
    end
    object edtCantidad: TEdit
      Left = 384
      Top = 52
      Width = 121
      Height = 21
      TabOrder = 6
      Text = 'edtCantidad'
    end
  end
  object DBGrid1: TDBGrid
    Left = 24
    Top = 192
    Width = 585
    Height = 249
    DataSource = DataSource1
    TabOrder = 0
    TitleFont.Charset = DEFAULT_CHARSET
    TitleFont.Color = clWindowText
    TitleFont.Height = -11
    TitleFont.Name = 'MS Sans Serif'
    TitleFont.Style = []
  end
  object GroupBox1: TGroupBox
    Left = 656
    Top = 200
    Width = 297
    Height = 249
    Caption = '3'
    TabOrder = 1
    object Label3: TLabel
      Left = 83
      Top = 24
      Width = 70
      Height = 13
      Caption = 'Codigo destino'
    end
    object Label4: TLabel
      Left = 19
      Top = 72
      Width = 62
      Height = 13
      Caption = 'Precio desde'
    end
    object Label5: TLabel
      Left = 158
      Top = 72
      Width = 59
      Height = 13
      Caption = 'Precio hasta'
    end
    object Label6: TLabel
      Left = 91
      Top = 172
      Width = 118
      Height = 13
      Caption = 'Cantidad de propiedades'
    end
    object edtDestino2: TEdit
      Left = 88
      Top = 40
      Width = 121
      Height = 21
      TabOrder = 0
      Text = 'edtDestino2'
    end
    object edtPrecioDesde: TEdit
      Left = 160
      Top = 88
      Width = 121
      Height = 21
      TabOrder = 1
      Text = 'edtPrecioDesde'
    end
    object edtPrecioHasta: TEdit
      Left = 24
      Top = 88
      Width = 121
      Height = 21
      TabOrder = 2
      Text = 'edtPrecioHasta'
    end
    object Calcular: TButton
      Left = 118
      Top = 128
      Width = 75
      Height = 25
      Caption = 'Calcular'
      TabOrder = 3
      OnClick = CalcularClick
    end
    object edtCantidadProp: TEdit
      Left = 88
      Top = 188
      Width = 121
      Height = 21
      TabOrder = 4
      Text = 'edtCantidadProp'
    end
  end
  object GroupBox2: TGroupBox
    Left = 664
    Top = 16
    Width = 273
    Height = 105
    Caption = '2'
    TabOrder = 2
    object Label7: TLabel
      Left = 24
      Top = 32
      Width = 61
      Height = 13
      Caption = 'IDPropietario'
    end
    object edtIDPropietario: TEdit
      Left = 24
      Top = 48
      Width = 121
      Height = 21
      TabOrder = 0
      Text = 'edtIDPropietario'
    end
    object GenerarArchivo: TButton
      Left = 160
      Top = 40
      Width = 97
      Height = 33
      Caption = 'GenerarArchivo'
      TabOrder = 1
      OnClick = GenerarArchivoClick
    end
  end
  object tblPropiedades: TTable
    DatabaseName = 'd:\WendySclerandi'
    TableName = 'Propiedades.DB'
    Left = 8
    Top = 8
    object tblPropiedadesIDPropietario: TIntegerField
      FieldName = 'IDPropietario'
    end
    object tblPropiedadesIDPropiedad: TIntegerField
      FieldName = 'IDPropiedad'
    end
    object tblPropiedadesIDLocalidad: TIntegerField
      FieldName = 'IDLocalidad'
    end
    object tblPropiedadesDestino: TIntegerField
      FieldName = 'Destino'
    end
    object tblPropiedadesCantidadDormitorios: TIntegerField
      FieldName = 'CantidadDormitorios'
    end
    object tblPropiedadesGaraje: TBooleanField
      FieldName = 'Garaje'
    end
    object tblPropiedadesPatio: TBooleanField
      FieldName = 'Patio'
    end
    object tblPropiedadesMetrosCubiertos: TFloatField
      FieldName = 'MetrosCubiertos'
    end
    object tblPropiedadesPrecioVenta: TCurrencyField
      FieldName = 'PrecioVenta'
    end
    object tblPropiedadesDomicilio: TStringField
      FieldName = 'Domicilio'
      Size = 50
    end
    object tblPropiedadesEstado: TIntegerField
      FieldName = 'Estado'
    end
  end
  object tblPropietarios: TTable
    DatabaseName = 'd:\WendySclerandi'
    TableName = 'Propietarios.db'
    Left = 40
    Top = 8
    object tblPropietariosIDPropietario: TIntegerField
      FieldName = 'IDPropietario'
    end
    object tblPropietariosNombre: TStringField
      FieldName = 'Nombre'
      Size = 50
    end
    object tblPropietariosTelefono: TStringField
      FieldName = 'Telefono'
      Size = 50
    end
    object tblPropietariosDomicilio: TStringField
      FieldName = 'Domicilio'
      Size = 50
    end
  end
  object DataSource1: TDataSource
    DataSet = tblPropiedades
    Left = 72
    Top = 8
  end
  object MainMenu1: TMainMenu
    Left = 8
    Top = 40
    object Ejercicio11: TMenuItem
      Caption = 'Ejercicio 1'
      OnClick = Ejercicio11Click
    end
    object Ejercicio21: TMenuItem
      Caption = 'Ejercicio 2'
      OnClick = Ejercicio21Click
    end
    object Ejercicio31: TMenuItem
      Caption = 'Ejercicio 3'
    end
  end
end
