#Encrypt by Sumarr ID
#Gitlab : Https://gitlab.com/Sumarr-ID
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))