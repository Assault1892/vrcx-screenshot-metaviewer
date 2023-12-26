import sys
import struct
import json

file_path = sys.argv[1]


def read_chunk_data(file_path, offset):
    with open(file_path, "rb") as file:
        # ファイルの先頭から指定のオフセットまでシーク
        file.seek(offset)

        # チャンクの長さを読み取る
        length_data = file.read(4)
        length = struct.unpack("!I", length_data)[0]

        # チャンクタイプを読み取る
        type_data = file.read(4)
        chunk_type = type_data.decode("ascii")

        # チャンクデータを読み取る
        chunk_data = file.read(length)

        return length, chunk_type, chunk_data


def display_chunk_data(file_path, offset):
    length, chunk_type, chunk_data = read_chunk_data(file_path, offset)
    str_data = chunk_data[16:]
    json_data = json.loads(str_data)

    print(f"Length: {length}")
    print(f"Type: {chunk_type}")
    # print(f"Data: {str_data}")
    print(f"Data: {json.dumps(json_data, indent=4)}")


# ファイルパスとオフセットを指定してチャンクデータを表示
offset = 33
display_chunk_data(file_path, offset)
