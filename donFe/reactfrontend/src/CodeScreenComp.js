import "./App.css";
import Editor from "@monaco-editor/react";
import { useState, useEffect, useRef } from "react";
import { useLocation } from "react-router-dom";
import Sk from "skulpt";

export default function CodeScreenComp({ height }) {
  let location = useLocation();
  let state = location.state;
  console.log("state");
  console.log(state);
  console.log(state.gamecode);
  const editorRef = useRef(null);
  const [outputs, setOutputs] = useState([]);
  const [answer, setAnswer] = useState();
  const [failedCase, setFailedCase] = useState("");

  function handleEditorDidMount(editor, monaco) {
    editorRef.current = editor;
  }
  // function submitPressed() {
  //   var code = editorRef.current.getValue();
  //   fetch("/api/test").then((response) => console.log(response.json()));
  // }
  const runCode = (input, output) => {
    var code = editorRef.current.getValue();
    console.log(code);
    code = code.concat(`\n\nprint(solution(${input}))`);

    const tempOutputs = [];

    // Create Skulpt configuration
    const skulptConfig = {
      output: (text) => {
        tempOutputs.push(text); // Store the output in a temporary array
      },
      //   read: () => {
      //     // Dummy implementation for input
      //     return window.prompt("Enter input:");
      //   },
    };

    // Clear any previous Skulpt session
    Sk.resetCompiler();

    // Execute Python code using Skulpt
    Sk.configure(skulptConfig);
    const module = Sk.importMainWithBody("<stdin>", false, code);

    // Update the state with the collected outputs
    setAnswer(tempOutputs.at(-1).trim());
    console.log(`the last of the output ${tempOutputs},${tempOutputs.at(-1)}`);
    setOutputs(tempOutputs.slice(0, -1));

    console.log("output bellow");
    console.log(tempOutputs);
    return tempOutputs.at(-1).trim() === output;
  };

  function submitPressed() {
    console.log(`game code ${state.gamecode}`);

    fetch("/api/getTests", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ gamecode: state.gamecode }),
    }).then((resp) => {
      console.log(resp);
    });
    console.log("setting the array to be empty");
    setFailedCase(0);
    for (let i = 0; i < state.testInputs.length; i++) {
      console.log("state");
      console.log(state);
      var result = runCode(state.testInputs[i], state.testOutputs[i]);
      console.log("ran");
      if (result == false) {
        console.log("failed testcase");
        setFailedCase([state.testInputs[i], state.testOutputs[i]]);
        break;
      }
    }
  }
  return (
    <div style={{ height: "100%" }}>
      <div className="info">
        <h1 className="'infochild">{state.title}</h1>
        <h1 className="'infochild">{state.userName}</h1>
      </div>
      <div style={{ height: "100%" }}>
        <Editor
          height="auto"
          theme="vc"
          onMount={handleEditorDidMount}
          language="python"
          path="solution.py"
          value={"def solution"}
        />
      </div>
      <p>{state.desc}</p>
      <button onClick={submitPressed}>
        <p>Submit Your Answer</p>
      </button>

      <div class="terminal">
        {outputs.map((output, index) => (
          <pre key={index}>{`>> ${output}`}</pre> // Display each output
        ))}
      </div>
      <div>
        <p>
          {failedCase === 0
            ? "all test cases passed"
            : failedCase !== ""
            ? `failed test case: ${failedCase[0]} your output: ${answer} expected: ${failedCase[1]}`
            : ""}
        </p>
      </div>
    </div>
  );
}
