const version = '0.0.1';

void main(List<String> arguments) {
  if (arguments.isEmpty || arguments.first == 'help') {
    printUsage();
  } else if (arguments.first == 'version') {
    print('Dartpedia CLI version $version');
  } else if (arguments.first == 'search') {
    final inputArgs = arguments.length > 1 ? arguments.sublist(1) : null;
    searchwikipedia(inputArgs);

    print('Search command recognized!');
  } else {
    printUsage();
  }
}

void searchwipedia(List<String>? arguments) {
  print('searchwikipedia received argments: $arguments');
}

void printUsage() {
  // Add this new function
  print(
    "The following commands are valid: 'help', 'version', 'search <ARTICLE-TITLE>'",
  );
}
