import React from 'react';
import Editor from "@monaco-editor/react";
import { useState, useEffect, useRef } from "react";

function SmallEditor(){
      const editorRef = useRef(null);
          function handleEditorDidMount(editor, monaco) {
    editorRef.current = editor;
  }
    return(
        <div>
            <
        </div>
    )
}