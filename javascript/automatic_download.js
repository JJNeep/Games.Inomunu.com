const productElement = document.getElementById('download_file');
let file = parseString(productElement.dataset.file);

window.onload = function() {
  document.getElementById('my_iframe').src = file;
};
