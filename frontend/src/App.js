import React, { useEffect, useMemo, useRef, useState } from 'react';
import {
  ArrowRight,
  BadgeCheck,
  BarChart3,
  Blocks,
  BookOpen,
  Bot,
  Building2,
  Check,
  ChevronDown,
  Globe,
  Headphones,
  Layers,
  MessageCircle,
  MessagesSquare,
  Send,
  ShieldCheck,
  Sparkles,
  Workflow,
} from 'lucide-react';
import './index.css';

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [openFaq, setOpenFaq] = useState('faq-1');
  const [isOnline, setIsOnline] = useState(false);
  const [isSending, setIsSending] = useState(false);
  const [chatInput, setChatInput] = useState('');
  const [chatMessages, setChatMessages] = useState([
    { role: 'assistant', content: 'Hi! Ask me anything — I’m ready.' },
  ]);
  const chatEndRef = useRef(null);

  useEffect(() => {
    const check = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/health`);
        const data = await res.json();
        setIsOnline(Boolean(data?.status === 'healthy'));
      } catch {
        setIsOnline(false);
      }
    };
    check();
    const t = setInterval(check, 5000);
    return () => clearInterval(t);
  }, []);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages, isSending]);

  const sendChat = async (text) => {
    const messageText = (text ?? chatInput).trim();
    if (!messageText || isSending) return;

    setChatInput('');
    setChatMessages((prev) => [...prev, { role: 'user', content: messageText }]);
    setIsSending(true);

    try {
      const res = await fetch(`${API_BASE_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: messageText }),
      });

      if (!res.ok) throw new Error('Chat request failed');
      const data = await res.json();

      setChatMessages((prev) => [
        ...prev,
        { role: 'assistant', content: data?.response ?? 'Sorry, I could not respond.' },
      ]);
    } catch {
      setChatMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content:
            'I can’t reach the backend. Start it on port 8000 (FastAPI) and try again.',
        },
      ]);
    } finally {
      setIsSending(false);
    }
  };

  const stats = useMemo(
    () => [
      { label: 'Avg. reply time', value: '<1s' },
      { label: 'Channels', value: 'Website + more' },
      { label: 'Setup time', value: 'Minutes' },
      { label: 'Support', value: '24/7' },
    ],
    []
  );

  const features = useMemo(
    () => [
      {
        icon: <Sparkles className="h-5 w-5" />,
        title: 'AI-generated replies',
        desc: 'Deliver helpful answers instantly with a modern conversational UX.',
      },
      {
        icon: <Workflow className="h-5 w-5" />,
        title: 'Flexible flows',
        desc: 'Handle FAQs, lead capture, and handoff paths without complexity.',
      },
      {
        icon: <BarChart3 className="h-5 w-5" />,
        title: 'Analytics built-in',
        desc: 'Track engagement, top questions, and conversion-friendly actions.',
      },
      {
        icon: <ShieldCheck className="h-5 w-5" />,
        title: 'Reliable & secure',
        desc: 'Designed for stability with a clean, production-ready layout.',
      },
      {
        icon: <MessagesSquare className="h-5 w-5" />,
        title: 'Great chat UI',
        desc: 'A premium chat experience your users will actually enjoy using.',
      },
      {
        icon: <Globe className="h-5 w-5" />,
        title: 'Multi-language ready',
        desc: 'A layout that scales globally with consistent spacing and type.',
      },
    ],
    []
  );

  const integrations = useMemo(
    () => [
      { name: 'Website', icon: <Globe className="h-4 w-4" /> },
      { name: 'Slack', icon: <Blocks className="h-4 w-4" /> },
      { name: 'Messenger', icon: <MessageCircle className="h-4 w-4" /> },
      { name: 'Shop', icon: <Building2 className="h-4 w-4" /> },
      { name: 'Helpdesk', icon: <Headphones className="h-4 w-4" /> },
      { name: 'CRM', icon: <Layers className="h-4 w-4" /> },
    ],
    []
  );

  const testimonials = useMemo(
    () => [
      {
        quote:
          'Clean design, fast setup, and the UI feels premium. Exactly what we needed for a modern support experience.',
        name: 'Product Lead',
        role: 'Customer Support',
      },
      {
        quote:
          'The landing page looks professional and converts better than our old “cartoon” layout. Big upgrade.',
        name: 'Founder',
        role: 'SaaS',
      },
      {
        quote:
          'Great structure: hero, social proof, and clear CTAs. It’s easy to extend with real content later.',
        name: 'Marketing Manager',
        role: 'Growth',
      },
    ],
    []
  );

  const faqs = useMemo(
    () => [
      {
        id: 'faq-1',
        q: 'Can I use this as just a frontend landing page?',
        a: 'Yes. This is a frontend-only landing page UI. You can connect it to any backend later.',
      },
      {
        id: 'faq-2',
        q: 'Can we add a “Try demo chat” section?',
        a: 'Yes. We can add a real chat widget or route to your existing chat screen when you’re ready.',
      },
      {
        id: 'faq-3',
        q: 'Can you match my brand colors?',
        a: 'Yes. Tell me your brand primary color + logo, and I’ll update the palette and typography.',
      },
    ],
    []
  );

  return (
    <div className="min-h-screen bg-[#0b0f19]">
      {/* background glow */}
      <div className="pointer-events-none fixed inset-0 -z-10">
        <div className="absolute -top-48 left-1/2 h-[520px] w-[520px] -translate-x-1/2 rounded-full bg-emerald-500/20 blur-[120px]" />
        <div className="absolute top-24 right-[-140px] h-[420px] w-[420px] rounded-full bg-indigo-500/20 blur-[110px]" />
      </div>

      {/* navbar */}
      <div className="sticky top-0 z-50 border-b border-white/10 bg-[#0b0f19]/70 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
          <div className="flex items-center gap-3">
            <div className="grid h-9 w-9 place-items-center rounded-xl bg-gradient-to-br from-emerald-400 to-emerald-600 shadow-[0_10px_30px_rgba(16,185,129,0.25)]">
              <Bot className="h-5 w-5 text-white" />
            </div>
            <div className="leading-tight">
              <div className="text-sm font-semibold text-white">AI Chatbot</div>
              <div className="text-xs text-white/60">Kavishka Dileepa</div>
            </div>
          </div>

          <div className="hidden items-center gap-6 text-sm text-white/70 md:flex">
            <a className="hover:text-white" href="#features">
              Features
            </a>
            <a className="hover:text-white" href="#integrations">
              Integrations
            </a>
            <a className="hover:text-white" href="#testimonials">
              Reviews
            </a>
            <a className="hover:text-white" href="#demo">
              Demo
            </a>
            <a className="hover:text-white" href="#faq">
              FAQ
            </a>
          </div>

          <div className="flex items-center gap-3">
            <div
              className={`hidden items-center gap-2 rounded-full border px-3 py-1 text-xs md:inline-flex ${
                isOnline
                  ? 'border-emerald-500/30 bg-emerald-500/10 text-emerald-200'
                  : 'border-red-500/30 bg-red-500/10 text-red-200'
              }`}
              title={isOnline ? 'Backend connected' : 'Backend offline'}
            >
              <span className={`h-2 w-2 rounded-full ${isOnline ? 'bg-emerald-400' : 'bg-red-400'}`} />
              {isOnline ? 'Online' : 'Offline'}
            </div>
            <a
              href="#pricing"
              className="hidden rounded-lg px-3 py-2 text-sm font-medium text-white/80 hover:text-white md:inline"
            >
              Pricing
            </a>
            <a
              href="#get-started"
              className="inline-flex items-center gap-2 rounded-lg bg-white px-3 py-2 text-sm font-semibold text-[#0b0f19] hover:bg-white/90"
            >
              Get started <ArrowRight className="h-4 w-4" />
            </a>
          </div>
        </div>
      </div>

      {/* hero */}
      <section className="mx-auto max-w-6xl px-4 pt-14 pb-10 md:pt-20">
        <div className="grid gap-10 md:grid-cols-2 md:items-center">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-medium text-white/70">
              <BadgeCheck className="h-4 w-4 text-emerald-400" />
              Modern, conversion-focused frontend
            </div>

            <h1 className="mt-5 text-4xl font-bold tracking-tight text-white md:text-5xl">
              Help, convert, and support with a <span className="text-emerald-400">clean AI chatbot</span> experience
            </h1>

            <p className="mt-4 text-base leading-relaxed text-white/70">
              A premium landing page UI inspired by modern SaaS design (like{' '}
              <a className="underline decoration-white/20 hover:text-white" href="https://www.chatbot.com/" target="_blank" rel="noreferrer">
                chatbot.com
              </a>
              ) — built for your project, without the “cartoon” feel.
            </p>

            <div className="mt-7 flex flex-col gap-3 sm:flex-row sm:items-center">
              <a
                href="#get-started"
                className="inline-flex items-center justify-center gap-2 rounded-xl bg-emerald-500 px-5 py-3 text-sm font-semibold text-white shadow-[0_12px_30px_rgba(16,185,129,0.25)] hover:bg-emerald-400"
              >
                Start free <ArrowRight className="h-4 w-4" />
              </a>
              <a
                href="#features"
                className="inline-flex items-center justify-center gap-2 rounded-xl border border-white/10 bg-white/5 px-5 py-3 text-sm font-semibold text-white/80 hover:bg-white/10 hover:text-white"
              >
                See features <ChevronDown className="h-4 w-4" />
              </a>
            </div>

            <div className="mt-8 grid grid-cols-2 gap-3 sm:grid-cols-4">
              {stats.map((s) => (
                <div key={s.label} className="rounded-xl border border-white/10 bg-white/5 p-4">
                  <div className="text-lg font-bold text-white">{s.value}</div>
                  <div className="mt-1 text-xs text-white/60">{s.label}</div>
                </div>
              ))}
            </div>
          </div>

          {/* hero mock */}
          <div className="relative">
            <div className="rounded-2xl border border-white/10 bg-gradient-to-b from-white/10 to-white/5 p-5 shadow-[0_25px_60px_rgba(0,0,0,0.45)]">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="grid h-10 w-10 place-items-center rounded-xl bg-gradient-to-br from-emerald-400 to-emerald-600">
                    <Sparkles className="h-5 w-5 text-white" />
                  </div>
                  <div>
                    <div className="text-sm font-semibold text-white">AI Chatbot</div>
                    <div className="text-xs text-white/60">Online • replies instantly</div>
                  </div>
                </div>
                <div className="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-white/70">
                  Demo UI
                </div>
              </div>

              <div className="mt-5 space-y-3">
                <div className="w-fit max-w-[88%] rounded-2xl border border-white/10 bg-[#0b0f19]/60 px-4 py-3 text-sm text-white/80">
                  Hi! How can I help you today?
                </div>
                <div className="ml-auto w-fit max-w-[88%] rounded-2xl bg-gradient-to-br from-indigo-500 to-fuchsia-500 px-4 py-3 text-sm text-white">
                  I need a professional chatbot landing page.
                </div>
                <div className="w-fit max-w-[88%] rounded-2xl border border-white/10 bg-[#0b0f19]/60 px-4 py-3 text-sm text-white/80">
                  Done. Clean layout, social proof, strong CTA, and sections you can customize.
                </div>
              </div>

              <div className="mt-5 flex items-center gap-2 rounded-xl border border-white/10 bg-white/5 px-3 py-3">
                <div className="text-sm text-white/50">Message…</div>
                <div className="ml-auto grid h-9 w-9 place-items-center rounded-lg bg-white text-[#0b0f19]">
                  <ArrowRight className="h-4 w-4" />
                </div>
              </div>
            </div>

            <div className="pointer-events-none absolute -bottom-8 -left-8 hidden h-24 w-24 rounded-3xl bg-emerald-500/20 blur-2xl md:block" />
          </div>
        </div>
      </section>

      {/* logos / social proof */}
      <section id="integrations" className="mx-auto max-w-6xl px-4 pb-14">
        <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
          <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
            <div>
              <div className="text-sm font-semibold text-white">Support customers on multiple channels</div>
              <div className="text-sm text-white/60">
                Add the chatbot UI to your website or connect integrations later.
              </div>
            </div>
            <div className="text-xs text-white/50">Frontend-only demo • Replace with real logos anytime</div>
          </div>

          <div className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-6">
            {integrations.map((i) => (
              <div
                key={i.name}
                className="flex items-center justify-center gap-2 rounded-xl border border-white/10 bg-[#0b0f19]/40 px-3 py-3 text-sm text-white/70"
              >
                <span className="text-white/70">{i.icon}</span>
                <span className="font-medium">{i.name}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* features */}
      <section id="features" className="mx-auto max-w-6xl px-4 pb-14">
        <div className="max-w-2xl">
          <div className="text-xs font-semibold uppercase tracking-wider text-emerald-400">Features</div>
          <h2 className="mt-2 text-3xl font-bold text-white">Everything you need for a modern chatbot frontend</h2>
          <p className="mt-3 text-white/70">
            This is a clean, scalable UI foundation. You can plug in your actual chat backend later.
          </p>
        </div>

        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((f) => (
            <div key={f.title} className="rounded-2xl border border-white/10 bg-white/5 p-6">
              <div className="flex items-center gap-3">
                <div className="grid h-10 w-10 place-items-center rounded-xl bg-emerald-500/15 text-emerald-300">
                  {f.icon}
                </div>
                <div className="text-base font-semibold text-white">{f.title}</div>
              </div>
              <div className="mt-3 text-sm leading-relaxed text-white/70">{f.desc}</div>
            </div>
          ))}
        </div>
      </section>

      {/* pricing teaser */}
      <section id="pricing" className="mx-auto max-w-6xl px-4 pb-14">
        <div className="grid gap-4 md:grid-cols-3">
          <div className="rounded-2xl border border-white/10 bg-white/5 p-6 md:col-span-2">
            <div className="flex items-center gap-3">
              <div className="grid h-10 w-10 place-items-center rounded-xl bg-indigo-500/15 text-indigo-200">
                <Building2 className="h-5 w-5" />
              </div>
              <div>
                <div className="text-base font-semibold text-white">Flexible plans</div>
                <div className="text-sm text-white/60">Use this section as your pricing block.</div>
              </div>
            </div>
            <div className="mt-4 grid gap-3 sm:grid-cols-3">
              {[
                { name: 'Starter', price: 'Free', items: ['Landing page UI', 'Tailwind components', 'Responsive'] },
                { name: 'Pro', price: '$$', items: ['More sections', 'Brand theming', 'Polished animations'] },
                { name: 'Business', price: '$$$', items: ['Custom pages', 'SEO polish', 'Analytics UI'] },
              ].map((p) => (
                <div key={p.name} className="rounded-xl border border-white/10 bg-[#0b0f19]/40 p-4">
                  <div className="flex items-center justify-between">
                    <div className="text-sm font-semibold text-white">{p.name}</div>
                    <div className="text-xs text-white/60">{p.price}</div>
                  </div>
                  <div className="mt-3 space-y-2">
                    {p.items.map((it) => (
                      <div key={it} className="flex items-start gap-2 text-sm text-white/70">
                        <Check className="mt-0.5 h-4 w-4 text-emerald-400" />
                        <span>{it}</span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-2xl border border-white/10 bg-gradient-to-b from-emerald-500/15 to-white/5 p-6">
            <div className="flex items-center gap-3">
              <div className="grid h-10 w-10 place-items-center rounded-xl bg-emerald-500/20 text-emerald-200">
                <BookOpen className="h-5 w-5" />
              </div>
              <div>
                <div className="text-base font-semibold text-white">Quick setup</div>
                <div className="text-sm text-white/60">Ship a polished look fast.</div>
              </div>
            </div>
            <div className="mt-4 space-y-3 text-sm text-white/75">
              <div className="flex items-start gap-2">
                <Check className="mt-0.5 h-4 w-4 text-emerald-300" />
                Replace text with your real product copy
              </div>
              <div className="flex items-start gap-2">
                <Check className="mt-0.5 h-4 w-4 text-emerald-300" />
                Add your logo + brand color in minutes
              </div>
              <div className="flex items-start gap-2">
                <Check className="mt-0.5 h-4 w-4 text-emerald-300" />
                Extend to a full app later
              </div>
            </div>
            <a
              href="#get-started"
              className="mt-6 inline-flex w-full items-center justify-center gap-2 rounded-xl bg-emerald-500 px-5 py-3 text-sm font-semibold text-white hover:bg-emerald-400"
            >
              Get started <ArrowRight className="h-4 w-4" />
            </a>
          </div>
        </div>
      </section>

      {/* testimonials */}
      <section id="testimonials" className="mx-auto max-w-6xl px-4 pb-14">
        <div className="max-w-2xl">
          <div className="text-xs font-semibold uppercase tracking-wider text-emerald-400">Reviews</div>
          <h2 className="mt-2 text-3xl font-bold text-white">A UI your users will trust</h2>
          <p className="mt-3 text-white/70">Professional spacing, typography, and layout patterns.</p>
        </div>

        <div className="mt-8 grid gap-4 md:grid-cols-3">
          {testimonials.map((t, idx) => (
            <div key={idx} className="rounded-2xl border border-white/10 bg-white/5 p-6">
              <div className="text-sm leading-relaxed text-white/80">“{t.quote}”</div>
              <div className="mt-5 flex items-center justify-between">
                <div>
                  <div className="text-sm font-semibold text-white">{t.name}</div>
                  <div className="text-xs text-white/60">{t.role}</div>
                </div>
                <div className="grid h-10 w-10 place-items-center rounded-xl bg-white/5 text-white/70">
                  <BadgeCheck className="h-5 w-5" />
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* demo chat */}
      <section id="demo" className="mx-auto max-w-6xl px-4 pb-14">
        <div className="max-w-2xl">
          <div className="text-xs font-semibold uppercase tracking-wider text-emerald-400">Demo</div>
          <h2 className="mt-2 text-3xl font-bold text-white">Try chatting right here</h2>
          <p className="mt-3 text-white/70">
            This uses your FastAPI backend at <span className="font-semibold text-white/80">{API_BASE_URL}</span>.
            Your Hugging Face token must be set on the backend (not in the browser).
          </p>
        </div>

        <div className="mt-8 grid gap-4 lg:grid-cols-5">
          <div className="lg:col-span-3">
            <div className="rounded-2xl border border-white/10 bg-white/5 p-5">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="grid h-10 w-10 place-items-center rounded-xl bg-gradient-to-br from-emerald-400 to-emerald-600">
                    <Sparkles className="h-5 w-5 text-white" />
                  </div>
                  <div>
                    <div className="text-sm font-semibold text-white">AI Chatbot</div>
                    <div className="text-xs text-white/60">
                      Status: {isOnline ? 'Connected' : 'Backend offline (start on port 8000)'}
                    </div>
                  </div>
                </div>
              </div>

              <div className="mt-5 h-[340px] overflow-y-auto rounded-xl border border-white/10 bg-[#0b0f19]/40 p-4">
                <div className="space-y-3">
                  {chatMessages.map((m, idx) => (
                    <div
                      key={idx}
                      className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}
                    >
                      <div
                        className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
                          m.role === 'user'
                            ? 'bg-gradient-to-br from-indigo-500 to-fuchsia-500 text-white'
                            : 'border border-white/10 bg-white/5 text-white/80'
                        }`}
                      >
                        {m.content}
                      </div>
                    </div>
                  ))}

                  {isSending && (
                    <div className="flex justify-start">
                      <div className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-white/60">
                        Thinking…
                      </div>
                    </div>
                  )}
                  <div ref={chatEndRef} />
                </div>
              </div>

              <div className="mt-4 flex items-end gap-3 rounded-xl border border-white/10 bg-white/5 p-3">
                <textarea
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' && !e.shiftKey) {
                      e.preventDefault();
                      sendChat();
                    }
                  }}
                  rows={1}
                  placeholder="Type your message…"
                  className="min-h-[44px] flex-1 resize-none bg-transparent px-2 py-2 text-sm text-white outline-none placeholder:text-white/40"
                />
                <button
                  type="button"
                  onClick={() => sendChat()}
                  disabled={!isOnline || isSending || chatInput.trim() === ''}
                  className={`inline-flex h-11 items-center justify-center gap-2 rounded-xl px-4 text-sm font-semibold transition ${
                    !isOnline || isSending || chatInput.trim() === ''
                      ? 'cursor-not-allowed bg-white/10 text-white/40'
                      : 'bg-emerald-500 text-white hover:bg-emerald-400'
                  }`}
                >
                  Send <Send className="h-4 w-4" />
                </button>
              </div>
            </div>
          </div>

          <div className="lg:col-span-2">
            <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
              <div className="text-sm font-semibold text-white">Backend setup (secure)</div>
              <div className="mt-2 text-sm leading-relaxed text-white/70">
                Set your Hugging Face token as an environment variable on the backend machine, then run the API.
              </div>

              <div className="mt-4 space-y-2 text-sm text-white/70">
                <div className="flex items-start gap-2">
                  <Check className="mt-0.5 h-4 w-4 text-emerald-400" />
                  Token stays on server (frontend never sees it)
                </div>
                <div className="flex items-start gap-2">
                  <Check className="mt-0.5 h-4 w-4 text-emerald-400" />
                  Frontend calls <span className="font-mono text-xs text-white/80">/api/chat</span>
                </div>
                <div className="flex items-start gap-2">
                  <Check className="mt-0.5 h-4 w-4 text-emerald-400" />
                  Works locally on <span className="font-mono text-xs text-white/80">localhost:8000</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="mx-auto max-w-6xl px-4 pb-14">
        <div className="max-w-2xl">
          <div className="text-xs font-semibold uppercase tracking-wider text-emerald-400">FAQ</div>
          <h2 className="mt-2 text-3xl font-bold text-white">Common questions</h2>
          <p className="mt-3 text-white/70">
            Want it even closer to the style on{' '}
            <a className="underline decoration-white/20 hover:text-white" href="https://www.chatbot.com/" target="_blank" rel="noreferrer">
              chatbot.com
            </a>
            ? Send me a screenshot of the exact sections you like.
          </p>
        </div>

        <div className="mt-8 space-y-3">
          {faqs.map((f) => {
            const isOpen = openFaq === f.id;
            return (
              <button
                key={f.id}
                type="button"
                onClick={() => setOpenFaq((prev) => (prev === f.id ? '' : f.id))}
                className="w-full rounded-2xl border border-white/10 bg-white/5 p-5 text-left hover:bg-white/10"
              >
                <div className="flex items-center justify-between gap-4">
                  <div className="text-sm font-semibold text-white">{f.q}</div>
                  <ChevronDown className={`h-5 w-5 text-white/60 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
                </div>
                {isOpen && <div className="mt-3 text-sm leading-relaxed text-white/70">{f.a}</div>}
              </button>
            );
          })}
        </div>
      </section>

      {/* CTA */}
      <section id="get-started" className="mx-auto max-w-6xl px-4 pb-16">
        <div className="rounded-3xl border border-white/10 bg-gradient-to-r from-emerald-500/15 via-white/5 to-indigo-500/15 p-8 md:p-10">
          <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
            <div className="max-w-2xl">
              <div className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-medium text-white/70">
                <BadgeCheck className="h-4 w-4 text-emerald-400" />
                Frontend ready
              </div>
              <h3 className="mt-4 text-2xl font-bold text-white md:text-3xl">
                Want this landing page to match your brand perfectly?
              </h3>
              <p className="mt-2 text-white/70">
                Tell me your primary color, logo text, and the sections you want to keep/remove — I’ll tailor it.
              </p>
            </div>
            <div className="flex flex-col gap-3 sm:flex-row">
              <a
                href="#features"
                className="inline-flex items-center justify-center gap-2 rounded-xl border border-white/10 bg-white/5 px-5 py-3 text-sm font-semibold text-white/80 hover:bg-white/10 hover:text-white"
              >
                View sections <ChevronDown className="h-4 w-4" />
              </a>
              <a
                href="#"
                onClick={(e) => e.preventDefault()}
                className="inline-flex items-center justify-center gap-2 rounded-xl bg-white px-5 py-3 text-sm font-semibold text-[#0b0f19] hover:bg-white/90"
              >
                Contact / CTA <ArrowRight className="h-4 w-4" />
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* footer */}
      <footer className="border-t border-white/10">
        <div className="mx-auto flex max-w-6xl flex-col gap-4 px-4 py-10 md:flex-row md:items-center md:justify-between">
          <div className="flex items-center gap-3">
            <div className="grid h-9 w-9 place-items-center rounded-xl bg-white/5">
              <Bot className="h-5 w-5 text-white/80" />
            </div>
            <div>
              <div className="text-sm font-semibold text-white">AI Chatbot</div>
              <div className="text-xs text-white/60">Made by Kavishka Dileepa</div>
            </div>
          </div>
          <div className="text-xs text-white/50">© 2026 All rights reserved</div>
        </div>
      </footer>
    </div>
  );
}

export default App;
