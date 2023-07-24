import "./App.css";
import Editor from "@monaco-editor/react";
import { useState, useRef } from "react";
import LoginScreen from "./Login";
import CodeScreen from "./CodeScreenComp";
import HomeScreen from "./Homescreen";
import CreateGameScreen from "./CreateGameScreen";
import HostScreen from "./HostScreen";
//PythonCodeRunner
import { BrowserRouter, Route, Routes } from "react-router-dom";

export default function App() {
  const [gameData, setGameData] = useState();
  function loginSubmitted(data) {
    if (data.valid == true) {
      console.log("valid code");
      //need to transition to code screen here
      setGameData(data);
    }
    // otherwise dont transition and remain at login
  }
  //   return <LoginScreen setGameData_={loginSubmitted} />;
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomeScreen />} />
        <Route path="/joingame" element={<LoginScreen />} />
        <Route path="/codescreen" element={<CodeScreen />} />
        <Route path="/creategame" element={<CreateGameScreen />} />
        <Route path="/hostScreen" element={<HostScreen />} />
      </Routes>
    </BrowserRouter>
  );
}
