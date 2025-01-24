[app]

# Nome do aplicativo
title = CryptoApp

# Nome do pacote
package.name = cryptoapp

# Domínio do pacote
package.domain = org.exemplo

# Versão do seu aplicativo
version = 1.0

# Descrição do aplicativo
description = Consulta de cotação de criptomoedas em tempo real

# Caminho de origem (diretório onde estão os arquivos Python do seu aplicativo)
source.dir = .

# Arquivos a serem incluídos no APK
source.include_exts = py,png,jpg,kv,atlas

# Bibliotecas necessárias
requirements = python3,kivy,requests

# Caminho do ícone
icon.filename = %(source.dir)/icon.png  # Certifique-se de ter o ícone (icon.png) na pasta raiz

# Modo de debug
debug = 1

# Plataforma alvo
target = android

# Arquitetura para Android
arch = armeabi-v7a

# Nível de log
log_level = 2

# Permissões do Android (necessária para acessar a internet)
android.permissions = INTERNET

# Versão mínima da API Android
android.minapi = 21  # Lollipop ou superior

# SDK e NDK do Android
android.sdk = 24
android.ndk = 19b

# Configurações de orientação
orientation = portrait
