import React from "react";
import "./App.css";
import Editor from "@monaco-editor/react";
import { useState, useRef } from "react";
import { BrowserRouter, Route, Link, useNavigate } from "react-router-dom";

export default function HomeScreen() {
  const navigate = useNavigate();

  return (
    <div>
      <button onClick={() => navigate("/creategame")}>Create Game</button>
      <button onClick={() => navigate("/joingame")}>Join Game</button>
    </div>
  );
}
