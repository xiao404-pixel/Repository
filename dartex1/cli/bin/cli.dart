const version = '0.0.1';

void main(List<String> arguments) {
  if (arguments.isEmpty || arguments.first == 'help') {
    printUsage();
  } else if (arguments.first == 'version') {
    print('Dartpedia CLI version $version');

    // 新增下列兩行
  } else if (arguments.first == 'search') {
    print('Search command recognized!');
  } else {
    printUsage();
  }
}

void printUsage() {
  // Add this new function
  print(
    "The following commands are valid: 'help', 'version', 'search <ARTICLE-TITLE>'",
  );
}
