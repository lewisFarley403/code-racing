import "./App.css";
import Editor from "@monaco-editor/react";
import { useState, useRef } from "react";
import { BrowserRouter, Route, Link, useNavigate } from "react-router-dom";

export default function LoginScreen({ setGameData_ }) {
  const [gameCode, setGameCode] = useState();
  const [errors, setErrors] = useState("");

  const [userName, setUserName] = useState("");
  const navigate = useNavigate();
  function handleData(data) {
    console.log(data);
    if (data.error !== "") {
      setErrors(data.error);
      alert(data.error);
    } else {
      console.log(`errors ${errors}`);
      navigate("/codescreen", { state: data.gamedata });
    }
  }

  function submitClick() {
    fetch("/api/registerPlayer", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: userName, gamecode: gameCode }),
    })
      .then((resp) => resp.json())
      .then((data) => {
        // console.log(data);
        // console.log(data.error);
        console.log("setting error");
        handleData(data);
      });
  }
  // function getGameData() {
  //   fetch("/api/getGameData", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify({ gamecode: gameCode }),
  //   })
  //     .then((resp) => resp.json())
  //     .then((data) => {
  //       data.gameCode = gameCode;
  //       data.userName = userName;
  //       handleData(data);

  //       console.log(data);
  //     });
  // }

  return (
    <div>
      <input
        onChange={(e) => setGameCode(e.target.value)}
        type="number"
      ></input>
      <label>Please enter your game pin</label>
      <br></br>

      <input onChange={(e) => setUserName(e.target.value)}></input>
      <label>Please enter your display name</label>
      <br></br>
      <button onClick={submitClick}>Submit</button>
      <p>{errors}</p>
    </div>
  );
}
