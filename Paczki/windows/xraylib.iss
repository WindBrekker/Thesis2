; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#ifdef XRL64
#define MyAppName "xraylib 64-bit"
#define MyAppId "xraylib_64"
#define srcdir abs_top_srcdir_win
#define builddir abs_top_builddir_win
#else
#define MyAppName "xraylib 32-bit"
#define MyAppId "xraylib"
#define srcdir abs_top_srcdir_win
#define builddir abs_top_builddir_win
#endif
#define MyAppPublisher "Tom Schoonjans"
#define MyAppURL "http://github.com/tschoonj/xraylib"


[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
;AppId={{09253190-AB34-4A62-9A2A-930AE94FCF32}
AppName={#MyAppName}
AppId={#MyAppId}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={commonpf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
LicenseFile={#srcdir}\windows\License.rtf
OutputDir={#builddir}\windows
#ifdef XRL64
OutputBaseFilename=xraylib-{#MyAppVersion}-win64
ArchitecturesInstallIn64BitMode=x64
ArchitecturesAllowed=x64
#else
OutputBaseFilename=xraylib-{#MyAppVersion}-win32
#endif
Compression=lzma
ChangesEnvironment=yes
SetupLogging=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Types]
Name: "minimal" ; Description: "Minimal installation"
Name: "full" ; Description: "Full installation"
Name: "custom" ; Description: "Custom installation" ; Flags: iscustom

[Components]
Name: "core" ; Description: "xraylib shared library and documentation" ; Flags: fixed ; Types: full minimal custom
Name: "sdk" ; Description: "SDK: headers and static libraries" ; Types: full 
Name: "cplusplus" ;  Description: "C++ header-only bindings" ; Types: full
Name: "dotnet" ; Description: ".NET/C# bindings" ; Types: full 
Name: "pascal" ; Description: "Delphi/Pascal" ; Types: full

[Files]
Source: "{#builddir}\src\.libs\libxrl-{#LIB_CURRENT_MINUS_AGE}.dll"; DestDir: "{sys}" ; Flags: sharedfile ; Components: core
Source: "{#builddir}\windows\README.txt" ; DestDir: "{app}" ; Flags: isreadme ; Components: core
Source: "{#builddir}\windows\AUTHORS.txt" ; DestDir: "{app}" ; Components: core
Source: "{#builddir}\windows\Changelog.txt" ; DestDir: "{app}" ; Components: core
Source: "{#builddir}\windows\TODO.txt" ; DestDir: "{app}" ; Components: core
Source: "{#builddir}\windows\xraydoc.txt" ; DestDir: "{app}\Doc" ; Components: core

Source: "{#builddir}\windows\libxrl-{#LIB_CURRENT_MINUS_AGE}.lib" ; DestDir: "{app}\Lib" ; Components: sdk
Source: "{#builddir}\windows\libxrl-{#LIB_CURRENT_MINUS_AGE}.exp" ; DestDir: "{app}\Lib" ; Components: sdk
Source: "{#builddir}\src\.libs\libxrl.dll.a" ; DestDir: "{app}\Lib" ; Components: sdk
Source: "{#builddir}\src\libxrl-{#LIB_CURRENT_MINUS_AGE}.def" ; DestDir: "{app}\Lib" ; Components: sdk
Source: "{#builddir}\windows\README2.txt" ; DestDir: "{app}\Doc" ; DestName: "README.txt";Components: sdk
Source: "{#builddir}\windows\xrlexample1.c" ; DestDir: "{app}\Example" ; Components: sdk
Source: "{#builddir}\windows\xrlexample6.cpp" ; DestDir: "{app}\Example" ; Components: cplusplus
Source: "{#builddir}\windows\xraylib.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-parser.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-lines.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-shells.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-auger.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-crystal-diffraction.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-defs.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-deprecated.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-error.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-nist-compounds.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-radionuclides.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib-aux.h" ; DestDir: "{app}\Include" ; Components: sdk
Source: "{#builddir}\windows\xraylib++.h" ; DestDir: "{app}\Include" ; Components: cplusplus

#ifdef XRL64
Source: "{#srcdir}\windows\dotNet64\XrayLib.NET.dll" ; DestDir: "{app}\Lib" ; Components: dotnet ; Flags: sharedfile
Source: "{#srcdir}\windows\dotNet64\XrayLib.NETCore.dll" ; DestDir: "{app}\Lib" ; Components: dotnet ; Flags: sharedfile
#else
Source: "{#srcdir}\windows\dotNet32\XrayLib.NET.dll" ; DestDir: "{app}\Lib" ; Components: dotnet ; Flags: sharedfile
Source: "{#srcdir}\windows\dotNet32\XrayLib.NETCore.dll" ; DestDir: "{app}\Lib" ; Components: dotnet ; Flags: sharedfile
#endif
Source: "{#builddir}\windows\xrlexample8.cs" ; DestDir: "{app}\Example" ; Components: dotnet
Source: "{#srcdir}\windows\dotNetSrc\Docs\Help\XrayLibNET.chm" ; DestDir: "{app}\Doc" ; Components: dotnet
Source: "{#srcdir}\windows\dotNetSrc\Docs\Help\XrayLibNETCore.chm" ; DestDir: "{app}\Doc" ; Components: dotnet

Source: "{#builddir}\windows\xraylib.pas" ; DestDir: "{app}\Pascal" ; Components: pascal
Source: "{#builddir}\windows\xraylib_const.pas" ; DestDir: "{app}\Pascal" ; Components: pascal
Source: "{#builddir}\windows\xraylib_iface.pas" ; DestDir: "{app}\Pascal" ; Components: pascal
Source: "{#builddir}\windows\xraylib_impl.pas" ; DestDir: "{app}\Pascal" ; Components: pascal
Source: "{#builddir}\windows\xrlexample14.pas" ; DestDir: "{app}\Pascal" ; Components: pascal

[Icons]
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

[UninstallDelete]
Type: dirifempty ; Name: "{app}"

[Registry]
Root: HKLM; Subkey: "Software\xraylib" ; ValueType: string ; ValueName: "" ; ValueData: "{app}" ; Flags: uninsdeletekey

[Code]
/////////////////////////////////////////////////////////////////////
function GetUninstallString(): String;
var
  sUnInstPath: String;
  sUnInstallString: String;
begin
  sUnInstallString := '';
#ifdef XRL64
  sUnInstPath := ExpandConstant('Software\Microsoft\Windows\CurrentVersion\Uninstall\xraylib_64_is1');
#else
  sUnInstPath := ExpandConstant('Software\Microsoft\Windows\CurrentVersion\Uninstall\xraylib_is1');
#endif
  if not RegQueryStringValue(HKLM, sUnInstPath, 'UninstallString', sUnInstallString) then
    begin
    sUnInstPath := ExpandConstant('Software\Microsoft\Windows\CurrentVersion\Uninstall\xraylib');
    RegQueryStringValue(HKLM, sUnInstPath, 'QuietUninstallString', sUnInstallString);
  end
  else
  begin
	//innosetups QuietUninstallString is not as silent as I would like...
	sUnInstallString := sUnInstallString + ' /VERYSILENT';
  end;
  Log('QuietUninstallString: '+ sUnInstallString);
  Result := sUnInstallString;
end;


/////////////////////////////////////////////////////////////////////
function IsUpgrade(): Boolean;
begin
  Result := (GetUninstallString() <> '');
end;


/////////////////////////////////////////////////////////////////////
function UnInstallOldVersion(): Integer;
var
  sUnInstallString: String;
  iResultCode: Integer;
begin
// Return Values:
// 1 - uninstall string is empty
// 2 - error executing the UnInstallString
// 3 - successfully executed the UnInstallString

  // default return value
  Result := 0;

  // get the uninstall string of the old app
  sUnInstallString := GetUninstallString();
  if sUnInstallString <> '' then begin
    //sUnInstallString := RemoveQuotes(sUnInstallString);
    if Exec('>',sUnInstallString,'', SW_HIDE, ewWaitUntilTerminated, iResultCode) then
      Result := 3
    else
      Result := 2;
  end else
    Result := 1;
end;

function InitializeSetup(): Boolean;

begin
  Result := True;
  if (IsUpgrade()) then
  begin
    //launch dialog when not operating in silent mode
      if (WizardSilent()) then
      begin
        UnInstallOldVersion();
      end
      else
      begin
	//display msgbox
	if (MsgBox('A previously installed version of xraylib was found on the system. It has to be uninstalled before the installation can proceed.', mbConfirmation, MB_OKCANCEL)) = IDOK then
	begin
        	UnInstallOldVersion();
	end
	else
	begin
  		Result := False;
	end;
      end;
  end;
end;


procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
var
  BinDir, Path: String;
begin
  if (CurUninstallStep = usPostUninstall)
     and (RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'IDL_DLM_PATH', Path)) then
  begin
    BinDir := ExpandConstant('{app}\dlm');
    if Pos(';' + LowerCase(BinDir), Lowercase(Path)) <> 0 then
    begin
      StringChange(Path, ';' + BinDir, '');
      if CompareStr(Path,'<IDL_DEFAULT>') = 0 then
      begin
	RegDeleteValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'IDL_DLM_PATH')
      end
      else
      begin
        RegWriteStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'IDL_DLM_PATH', Path);
      end
    end;
  end;
  if (CurUninstallStep = usPostUninstall)
     and (RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'IDL_PATH', Path)) then
  begin
    BinDir := ExpandConstant('{app}\pro');
    if Pos(';' + LowerCase(BinDir), Lowercase(Path)) <> 0 then
    begin
      StringChange(Path, ';' + BinDir, '');
      if CompareStr(Path,'<IDL_DEFAULT>') = 0 then
      begin
	RegDeleteValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'IDL_PATH')
      end
      else
      begin
        RegWriteStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'IDL_PATH', Path);
      end
    end;
  end;
end;

