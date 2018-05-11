program Project1;

uses
  Forms,
  Unit1 in 'Unit1.pas' {frmEjercicio1},
  Unit2 in 'Unit2.pas' {frmEjercicio2},
  Unit3 in 'Unit3.pas' {frmEjercicio3};

{$R *.RES}

begin
  Application.Initialize;
  Application.CreateForm(TfrmEjercicio1, frmEjercicio1);
  Application.CreateForm(TfrmEjercicio2, frmEjercicio2);
  Application.CreateForm(TfrmEjercicio3, frmEjercicio3);
  Application.Run;
end.
