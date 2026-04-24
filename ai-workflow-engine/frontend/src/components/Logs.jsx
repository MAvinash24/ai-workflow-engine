export default function Logs({ logs }) {
  return (
    <div>
      <h2>Execution Logs</h2>
      {logs.map((log, i) => (
        <div key={i} style={{ border: "1px solid gray", margin: 10 }}>
          <p><b>Step:</b> {log.step}</p>
          <p><b>Result:</b> {log.result}</p>
          <p><b>Evaluation:</b> {log.evaluation}</p>
        </div>
      ))}
    </div>
  );
}