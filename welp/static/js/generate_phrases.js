function generate_phrase(convince_level) {
  var data = words;
  var phrase = generate_food(convince_level, data);
  if (Math.random() < (convince_level * 0.3)) {
    phrase = phrase.concat(generate_service(convince_level, data));  
  }
  if (Math.random() < (convince_level * 0.3)) { 
    phrase = phrase.concat(generate_other(convince_level, data));
  }
  return phrase
}

function generate_food(convince_level, data) {
  return "  The food was ".concat(words[convince_level]["food"][Math.floor(Math.random() *
  (words[convince_level]["food"].length))]).concat(".");
}

function generate_service(convince_level, data) {
  return "  Also, The service was ".concat(words[convince_level]["service"][Math.floor(Math.random() *
  (words[convince_level]["service"].length))]).concat(".");
}

function generate_other(convince_level, data) {
  return "  I'd also like to say that the ".concat(words["nouns"][Math.floor(Math.random() * words["nouns"].length)] + 
          " was ").concat(words[convince_level]["other"][Math.floor(Math.random()*words[convince_level]["other"].length)]).concat(".");
}



