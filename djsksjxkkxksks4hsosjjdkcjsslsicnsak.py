import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))