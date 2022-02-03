import React from "react";

type PromiseState =
  | { status: "initial" }
  | { status: "loading" }
  | { status: "successfull"; data: unknown }
  | { status: "failed"; error: string };

export const App: React.FC = () => {
  const [requestState, setRequestState] = React.useState<PromiseState>({
    status: "initial",
  });

  React.useEffect(() => {
    setRequestState({ status: "loading" });
    fetchHealthCheck()
      .then((response) => {
        if (response.status !== 200) {
          throw new Error(`Api Request failed with status: ${response.status}`);
        }
        return response.json();
      })
      .then((responseJson) => {
        setRequestState({ status: "successfull", data: responseJson });
      })
      .catch((error) => {
        setRequestState({ status: "failed", error: error });
      });
  }, []);

  return (
    <>
      <h1>App</h1>
      <div>
        <span>Request State:</span>
        <span>{requestState.status}</span>
        {requestState.status === "failed" && (
          <span>{requestState.error.toString()}</span>
        )}
        {requestState.status === "successfull" && (
          <span>{JSON.stringify(requestState.data)}</span>
        )}
      </div>
    </>
  );
};

async function fetchHealthCheck() {
  const response = await fetch(`${process.env.API_BASE_URL}doctors/health`);
  return response;
}
