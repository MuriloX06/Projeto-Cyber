@echo off
setlocal

REM Definir o caminho para o instalador
set "INSTALLER=Instalador do Gravador de Tela.exe"

REM Iniciar a instalação silenciosa e aguardar a conclusão
"%INSTALLER%" /VERYSILENT

REM Verificar se a instalação foi bem-sucedida e iniciar o aplicativo
if %ERRORLEVEL% equ 0 (
    start "" "%PROGRAMFILES(x86)%\Gravador de Tela\Gravador de Tela.exe"
) else (
    endlocal
)

REM Finalizar o script
endlocal
