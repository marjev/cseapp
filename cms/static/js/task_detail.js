function loadEditor() {
  const textarea = $('#solution')[0];
  CodeMirror.fromTextArea(textarea, {
    lineNumbers: true,
    readOnly: true
  });
};

const loadTask = async () => {
  loadEditor();
};

$(loadTask);
