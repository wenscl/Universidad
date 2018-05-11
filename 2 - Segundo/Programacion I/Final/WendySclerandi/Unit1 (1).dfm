object frmEjercicio1: TfrmEjercicio1
  Left = 261
  Top = 119
  Width = 1144
  Height = 692
  Caption = 'frmEjercicio1'
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
  object Label1: TLabel
    Left = 80
    Top = 120
    Width = 61
    Height = 13
    Caption = 'IDPropietario'
    FocusControl = DBEdit1
  end
  object Label2: TLabel
    Left = 80
    Top = 72
    Width = 59
    Height = 13
    Caption = 'IDPropiedad'
    FocusControl = DBEdit2
  end
  object Label3: TLabel
    Left = 80
    Top = 168
    Width = 57
    Height = 13
    Caption = 'IDLocalidad'
    FocusControl = DBEdit3
  end
  object Label4: TLabel
    Left = 80
    Top = 208
    Width = 36
    Height = 13
    Caption = 'Destino'
    FocusControl = DBEdit4
  end
  object Label5: TLabel
    Left = 80
    Top = 248
    Width = 94
    Height = 13
    Caption = 'CantidadDormitorios'
    FocusControl = DBEdit5
  end
  object Label6: TLabel
    Left = 80
    Top = 336
    Width = 76
    Height = 13
    Caption = 'MetrosCubiertos'
    FocusControl = DBEdit6
  end
  object Label7: TLabel
    Left = 80
    Top = 376
    Width = 58
    Height = 13
    Caption = 'PrecioVenta'
    FocusControl = DBEdit7
  end
  object Label8: TLabel
    Left = 80
    Top = 416
    Width = 42
    Height = 13
    Caption = 'Domicilio'
    FocusControl = DBEdit8
  end
  object Label9: TLabel
    Left = 80
    Top = 456
    Width = 33
    Height = 13
    Caption = 'Estado'
    FocusControl = DBEdit9
  end
  object Label10: TLabel
    Left = 152
    Top = 168
    Width = 83
    Height = 13
    Caption = 'NombreLocalidad'
    FocusControl = DBLookupComboBox1
  end
  object Label11: TLabel
    Left = 152
    Top = 120
    Width = 87
    Height = 13
    Caption = 'NombrePropietario'
    FocusControl = DBLookupComboBox2
  end
  object Label12: TLabel
    Left = 152
    Top = 208
    Width = 92
    Height = 13
    Caption = 'DescripcionDestino'
    FocusControl = edtDestino
  end
  object Label13: TLabel
    Left = 152
    Top = 456
    Width = 89
    Height = 13
    Caption = 'DescripcionEstado'
    FocusControl = edtEstado
  end
  object DBGrid1: TDBGrid
    Left = 424
    Top = 88
    Width = 625
    Height = 313
    DataSource = DataSource1
    TabOrder = 0
    TitleFont.Charset = DEFAULT_CHARSET
    TitleFont.Color = clWindowText
    TitleFont.Height = -11
    TitleFont.Name = 'MS Sans Serif'
    TitleFont.Style = []
  end
  object DBNavigator1: TDBNavigator
    Left = 496
    Top = 416
    Width = 440
    Height = 41
    DataSource = DataSource1
    ConfirmDelete = False
    TabOrder = 1
  end
  object DBEdit1: TDBEdit
    Left = 80
    Top = 136
    Width = 64
    Height = 21
    DataField = 'IDPropietario'
    DataSource = DataSource1
    TabOrder = 2
  end
  object DBEdit2: TDBEdit
    Left = 80
    Top = 88
    Width = 64
    Height = 21
    DataField = 'IDPropiedad'
    DataSource = DataSource1
    TabOrder = 3
  end
  object DBEdit3: TDBEdit
    Left = 80
    Top = 184
    Width = 64
    Height = 21
    DataField = 'IDLocalidad'
    DataSource = DataSource1
    TabOrder = 4
  end
  object DBEdit4: TDBEdit
    Left = 80
    Top = 224
    Width = 64
    Height = 21
    DataField = 'Destino'
    DataSource = DataSource1
    TabOrder = 5
  end
  object DBEdit5: TDBEdit
    Left = 80
    Top = 264
    Width = 64
    Height = 21
    DataField = 'CantidadDormitorios'
    DataSource = DataSource1
    TabOrder = 6
  end
  object DBCheckBox1: TDBCheckBox
    Left = 80
    Top = 288
    Width = 97
    Height = 17
    Caption = 'Garaje'
    DataField = 'Garaje'
    DataSource = DataSource1
    TabOrder = 7
    ValueChecked = 'True'
    ValueUnchecked = 'False'
  end
  object DBCheckBox2: TDBCheckBox
    Left = 80
    Top = 312
    Width = 97
    Height = 17
    Caption = 'Patio'
    DataField = 'Patio'
    DataSource = DataSource1
    TabOrder = 8
    ValueChecked = 'True'
    ValueUnchecked = 'False'
  end
  object DBEdit6: TDBEdit
    Left = 80
    Top = 352
    Width = 64
    Height = 21
    DataField = 'MetrosCubiertos'
    DataSource = DataSource1
    TabOrder = 9
  end
  object DBEdit7: TDBEdit
    Left = 80
    Top = 392
    Width = 64
    Height = 21
    DataField = 'PrecioVenta'
    DataSource = DataSource1
    TabOrder = 10
  end
  object DBEdit8: TDBEdit
    Left = 80
    Top = 432
    Width = 304
    Height = 21
    DataField = 'Domicilio'
    DataSource = DataSource1
    TabOrder = 11
  end
  object DBEdit9: TDBEdit
    Left = 80
    Top = 472
    Width = 64
    Height = 21
    DataField = 'Estado'
    DataSource = DataSource1
    TabOrder = 12
  end
  object DBLookupComboBox1: TDBLookupComboBox
    Left = 152
    Top = 184
    Width = 209
    Height = 21
    DataField = 'NombreLocalidad'
    DataSource = DataSource1
    TabOrder = 13
  end
  object DBLookupComboBox2: TDBLookupComboBox
    Left = 152
    Top = 136
    Width = 209
    Height = 21
    DataField = 'NombrePropietario'
    DataSource = DataSource1
    TabOrder = 14
  end
  object edtDestino: TDBEdit
    Left = 152
    Top = 224
    Width = 209
    Height = 21
    DataField = 'DescripcionDestino'
    DataSource = DataSource1
    TabOrder = 15
  end
  object edtEstado: TDBEdit
    Left = 152
    Top = 472
    Width = 233
    Height = 21
    DataField = 'DescripcionEstado'
    DataSource = DataSource1
    TabOrder = 16
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
  object tblLocalidades: TTable
    DatabaseName = 'd:\WendySclerandi'
    TableName = 'Localidades.db'
    Left = 72
    Top = 8
    object tblLocalidadesIDLocalidad: TIntegerField
      FieldName = 'IDLocalidad'
    end
    object tblLocalidadesNombreLocalidad: TStringField
      FieldName = 'NombreLocalidad'
      Size = 50
    end
  end
  object tblPropiedades: TTable
    BeforeInsert = tblPropiedadesBeforeInsert
    AfterInsert = tblPropiedadesAfterInsert
    BeforePost = tblPropiedadesBeforePost
    BeforeDelete = tblPropiedadesBeforeDelete
    OnCalcFields = tblPropiedadesCalcFields
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
    object tblPropiedadesNombreLocalidad: TStringField
      FieldKind = fkLookup
      FieldName = 'NombreLocalidad'
      LookupDataSet = tblLocalidades
      LookupKeyFields = 'IDLocalidad'
      LookupResultField = 'NombreLocalidad'
      KeyFields = 'IDLocalidad'
      Size = 50
      Lookup = True
    end
    object tblPropiedadesNombrePropietario: TStringField
      FieldKind = fkLookup
      FieldName = 'NombrePropietario'
      LookupDataSet = tblPropietarios
      LookupKeyFields = 'IDPropietario'
      LookupResultField = 'Nombre'
      KeyFields = 'IDPropietario'
      Size = 50
      Lookup = True
    end
    object tblPropiedadesDescripcionDestino: TStringField
      FieldKind = fkCalculated
      FieldName = 'DescripcionDestino'
      Size = 50
      Calculated = True
    end
    object tblPropiedadesDescripcionEstado: TStringField
      FieldKind = fkCalculated
      FieldName = 'DescripcionEstado'
      Size = 50
      Calculated = True
    end
  end
  object DataSource1: TDataSource
    DataSet = tblPropiedades
    Left = 8
    Top = 40
  end
  object MainMenu1: TMainMenu
    Left = 120
    Top = 8
    object Ejercicio11: TMenuItem
      Caption = 'Ejercicio 1'
    end
    object Ejercicio21: TMenuItem
      Caption = 'Ejercicio 2'
      OnClick = Ejercicio21Click
    end
    object Ejercicio31: TMenuItem
      Caption = 'Ejercicio 3'
      OnClick = Ejercicio31Click
    end
  end
end
