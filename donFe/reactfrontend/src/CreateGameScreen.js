import React from "react";
import "./creategame.css"; // Relative path to the CSS file

import { useEffect, useState } from "react";
import io from "socket.io-client";
import { BrowserRouter, Route, Link, useNavigate } from "react-router-dom";

export default function CreateGameScreen() {
  // useEffect(() => {
  //   const socket = io("/");

  //   // Listen for 'data_received' event
  //   socket.on(`${gamecode}playerjoin`, (data) => {
  //     console.log("Received data:", data);
  //     // Do something with the received data
  //   });

  //   // Clean up the socket connection when component unmounts
  //   return () => {
  //     socket.disconnect();
  //   };
  // }, []);
  const [questionData, setQuestionData] = useState([]);
  const [questionID, setQuestionID] = useState();
  const [joinCode, setJoinCode] = useState("");
  const navigate = useNavigate();
  function createGame() {
    fetch("/api/createGame", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ questionid: questionID }),
    })
      .then((resp) => resp.json())
      // .then((data) => setJoinCode(data.joinCode));
      .then((data) => {
        console.log(data.joinCode);
        navigate("/hostScreen", { state: data.joinCode });
      });
  }

  useEffect(() => {
    fetch("/api/getAllQuestions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((data) => data.json())
      .then((d) => {
        console.log(d);
        console.log(d.questions);
        setQuestionData(d.questions);
      });
  }, []);
  return (
    <div>
      <div className="table-container">
        <h2>Please select your question from the table</h2>
        <table className="data-table">
          <thead>
            <tr>
              <th>Question No</th>
              <th>Question Title</th>
              <th>Question Description</th>
            </tr>
          </thead>
          <tbody>
            {questionData.map((i, index) => (
              <tr
                className={
                  questionID - 1 === index ? "selected" : "nonselected"
                }
                onClick={(e) => {
                  console.log(`questionID ${questionID} index ${index}`);
                  console.log(`${index} clicked`);
                  console.log(questionID - 1 === index);
                  setQuestionID(index + 1);
                }}
                key={i[0]}
              >
                <td>{i[0]}</td>
                <td>{i[1]}</td>
                <td>{i[2]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button onClick={createGame}>Create Game</button>
      <h1>{joinCode}</h1>
    </div>
  );
}
