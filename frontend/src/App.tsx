import { Activity, AlertTriangle, Database, Network, Radar, Shield } from "lucide-react";

import { MetricCard } from "./components/MetricCard";

const roadmap = [
  "Log ingestion pipeline",
  "Threat rules engine",
  "AI incident analysis",
  "Alert management",
];

export default function App() {
  return (
    <main className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <Shield size={30} aria-hidden="true" />
          <div>
            <strong>AI SOC</strong>
            <span>Security Operations</span>
          </div>
        </div>
        <nav aria-label="Primary navigation">
          <a className="active" href="#overview">Overview</a>
          <a href="#events">Events</a>
          <a href="#alerts">Alerts</a>
          <a href="#rules">Rules</a>
          <a href="#reports">Reports</a>
        </nav>
      </aside>

      <section className="workspace">
        <header className="topbar">
          <div>
            <p className="eyebrow">Phase 1 Foundation</p>
            <h1>Security Operations Command Center</h1>
          </div>
          <button type="button">
            <Radar size={18} aria-hidden="true" />
            New Investigation
          </button>
        </header>

        <section className="metrics" aria-label="SOC metrics">
          <MetricCard label="Total Events" value="0" icon={Database} />
          <MetricCard label="Critical Alerts" value="0" icon={AlertTriangle} />
          <MetricCard label="Active Rules" value="0" icon={Activity} />
        </section>

        <section className="content-grid">
          <div className="panel primary-panel">
            <p className="eyebrow">Enterprise SOC Baseline</p>
            <h2>Build the SIEM foundation before detection logic</h2>
            <p>
              This project starts with a clean backend, database migration path, dashboard shell,
              and API structure ready for event ingestion, alert creation, rules, and AI analysis.
            </p>
            <div className="status-list">
              <span>FastAPI backend</span>
              <span>React TypeScript frontend</span>
              <span>PostgreSQL ready</span>
              <span>Alembic migrations</span>
            </div>
          </div>

          <div className="panel">
            <h2>Next SOC Capabilities</h2>
            <div className="roadmap">
              {roadmap.map((item) => (
                <article key={item}>
                  <Network size={20} aria-hidden="true" />
                  <span>{item}</span>
                </article>
              ))}
            </div>
          </div>
        </section>
      </section>
    </main>
  );
}
