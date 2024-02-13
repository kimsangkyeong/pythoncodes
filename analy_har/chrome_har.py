import os, sys
import codecs
from ast import literal_eval
import json

def main(argv):
  if len(argv) < 2 :
    print(f'\n Usage : python {argv[0]} file_names \n\tfile_names : chrome\'s trace logs => *.har \n')

  for filename in argv[1:]:
    split_filename = filename.split('.')
    if split_filename[len(split_filename)-1] != "har" :
      print(f'not suport file : {filename}')
    else :
      print(filename)
      try:
        f = codecs.open(filename, 'r', 'utf-8')
        data = f.read()
        f.close()

        # print(f'{type(data)}, {data[:10]}')
        # str to dictionary
        dict_data = json.loads(data)
        # print(f'{type(dict_data)} {dict_data["log"]["version"]}')
      except Exception as e:
        print(e)
      logs = "method \t url \t transferSize \t size \t mimeType \t status \t time \n";
      for entry in dict_data["log"]["entries"] :
        logs += "{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \n".format(
                entry["request"]["method"],
                entry["request"]["url"],
                entry["response"]["_transferSize"], # 네트워크를 통해서 다운로드 되는 파일 사이즈 (GZIP으로 압축된 용량)
                entry["response"]["content"]["size"], # GZIP 압축이 해제된 용량. 디스크에 저장되는 파일 용량
                entry["response"]["content"]["mimeType"], 
                entry["response"]["status"],
                entry["time"] 
              );
      print(f'{logs}')
      split_filename[len(split_filename)-1] = "csv"
      write_filename = '.'.join(split_filename)
      try:
        print(f' => {write_filename}')
        fw= open(write_filename, 'w+')
        fw.write(logs)
        fw.close()
      except Exception as e:
        print(e)

  return

if __name__ == "__main__":
  main(sys.argv[:])