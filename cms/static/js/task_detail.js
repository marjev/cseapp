const loadEditor = () => {
  const textarea = $('#solution')[0];
  const editor = CodeMirror.fromTextArea(textarea, {
    lineNumbers: true,
    readOnly: true
  });
};

$(loadEditor);
