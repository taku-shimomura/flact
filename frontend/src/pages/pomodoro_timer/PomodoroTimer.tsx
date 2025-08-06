import { useState, useEffect, useRef } from 'react';

export function PomodoroTimer() {
  const workDuration = 25 * 60;
  const breakDuration = 5 * 60;

  const [timeLeft, setTimeLeft] = useState(workDuration);
  const [isRunning, setIsRunning] = useState(false);
  const [isWorkSession, setIsWorkSession] = useState(true);
  const timerRef = useRef(null);

  const formatTime = (seconds) => {
    const m = String(Math.floor(seconds / 60)).padStart(2, '0');
    const s = String(seconds % 60).padStart(2, '0');
    return `${m}:${s}`;
  };

  useEffect(() => {
    if (isRunning) {
      timerRef.current = setInterval(() => {
        setTimeLeft((prev) => {
          if (prev === 0) {
            clearInterval(timerRef.current);
            const nextIsWork = !isWorkSession;
            setIsWorkSession(nextIsWork);
            setTimeLeft(nextIsWork ? workDuration : breakDuration);
            return nextIsWork ? workDuration : breakDuration;
          }
          return prev - 1;
        });
      }, 1000);
    }

    return () => clearInterval(timerRef.current);
  }, [isRunning, isWorkSession]);

  const handleStartPause = () => {
    setIsRunning(!isRunning);
  };

  const handleReset = () => {
    clearInterval(timerRef.current);
    setIsRunning(false);
    setIsWorkSession(true);
    setTimeLeft(workDuration);
  };

  return (
    <div>
      <h1>🍅 ポモドーロタイマー</h1>
      <h2>{isWorkSession ? '作業時間' : '休憩時間'}</h2>
      <div>{formatTime(timeLeft)}</div>
      <div>
        <button onClick={handleStartPause}>
          {isRunning ? '一時停止' : 'スタート'}
        </button>
        <button onClick={handleReset}>リセット</button>
      </div>
    </div>
  );
};

export default PomodoroTimer;
