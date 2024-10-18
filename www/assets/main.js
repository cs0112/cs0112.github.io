document.querySelectorAll('.stencil').forEach(function (stencil) {
  var sourceURL = stencil.getAttribute('data-source');
  var title = stencil.querySelector('.stencil-title');
  var copy = stencil.querySelector('.stencil-copy');
  var output = stencil.querySelector('.stencil-code');
  var source = null;

  // Unique identifier so that multiple copy clicks don't interfere with each
  // other.
  var copyJob = null;

  if (title && output) {
    title.addEventListener('click', handleExpand, false);
  }

  if (copy) {
    copy.addEventListener('click', handleCopy, false);
  }

  // Load source immediately since the copy-to-clipboard handler must operate
  // synchronously -- i.e. the code must already be loaded -- in order to have
  // permission to interact with the clipboard.
  loadSource(function() { });

  function loadSource(cb) {
    if (source !== null) return cb(source)

    var req = new XMLHttpRequest();
    req.addEventListener('load', done);
    req.open('GET', sourceURL, true);
    req.send();

    function done() {
      stencil.classList.add('stencil_loaded')
      source = req.responseText
      cb(source)
    }
  }

  function handleExpand (e) {
    e.preventDefault();
    if (stencil.classList.contains('stencil_expanded')) {
      stencil.classList.remove('stencil_expanded')
    } else {
      stencil.classList.add('stencil_expanded')
      loadSource(function(src) {
        output.innerHTML = src;
      })
    }
  }

  function handleCopy (e) {
    e.preventDefault();
    var job = {};
    copyJob = job;
    copy.classList.remove('stencil_copied');
    loadSource(function (src) {
      copyText(src, job);
    });
  }

  function copyText(text, job) {
    // https://stackoverflow.com/questions/400212/how-do-i-copy-to-the-clipboard-in-javascript
    if (!navigator.clipboard) return copyTextFallback(text, job);
    navigator.clipboard.writeText(text).then(function () {
      finishCopy(job);
    });
  }

  function copyTextFallback(text, job) {
    var textArea = document.createElement("textarea");
    textArea.value = text;
    
    // Avoid scrolling to bottom
    textArea.style.top = "0";
    textArea.style.left = "0";
    textArea.style.position = "fixed";
  
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try {
      document.execCommand('copy');
      finishCopy(job);
    } catch (err) {
      console.error('Unable to copy: ' + err);
    }
  
    document.body.removeChild(textArea);
  }

  function finishCopy(job) {
    if (copyJob !== job) return;

    copy.classList.add('stencil_copied');
    setTimeout(function () {
      if (copyJob === job) {
        copy.classList.remove('stencil_copied');
      }
    }, 750);
  }
})
