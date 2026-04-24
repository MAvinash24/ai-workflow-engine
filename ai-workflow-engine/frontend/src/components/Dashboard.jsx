import { useState } from "react";
import WorkflowRunner from "./WorkflowRunner";
import Logs from "./Logs";

export default function Dashboard() {
  const [logs, setLogs] = useState([]);

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Workflow Engine</h1>
      <WorkflowRunner setLogs={setLogs} />
      <Logs logs={logs} />
    </div>
  );
}