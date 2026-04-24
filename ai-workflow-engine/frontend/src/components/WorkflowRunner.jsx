import { useState } from "react";
import axios from "axios";

export default function WorkflowRunner({ setLogs }) {
  const [goal, setGoal] = useState("");

  const runWorkflow = async () => {
    const res = await axios.post("http://localhost:8000/run", { goal });
    setLogs(res.data.logs);
  };

  return (
    <div>
      <input
        value={goal}
        onChange={(e) => setGoal(e.target.value)}
        placeholder="Enter goal..."
      />
      <button onClick={runWorkflow}>Run</button>
    </div>
  );
}