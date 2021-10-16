import React from "react";

const DiffViewer = ({ diff, setShowDiffContainer }) => {
  const diffLines = diff.length ? diff.split("\n") : [];

  return (
    <div className={"diffContainer code-block"}>
      <button
        className={"close-btn"}
        onClick={() => setShowDiffContainer(false)}
      >
        <img src="https://image.flaticon.com/icons/png/512/1828/1828778.png" className={'btn-icon'} />
      </button>
      {diffLines.map((line, idx) => {
        let lineColor = "diff-line";

        if (line.startsWith("+")) {
          lineColor = "diff-line-added";
        } else if (line.startsWith("-")) {
          lineColor = "diff-line-remove";
        }

        return (
          <code key={idx} id={lineColor}>
            {line}
          </code>
        );
      })}
    </div>
  );
};

export default DiffViewer;
