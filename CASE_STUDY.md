# Integration QA case study / Entegrasyon QA vaka çalışması

## Test environment / Test ortamı

- Date / Tarih: 2026-11-04
- Hardware / Donanım: Apple Silicon M4
- Software / Yazılım: Claude-Mem 15.9.0; Codex CLI 0.166.0; Bun 1.4.4; uv 0.13.7
- Storage / Depolama: local Worker; cloud sync off

## Question / Soru

**EN:** Why are prompts searchable across Codex sessions while execution observations and summaries are not visible?

**TR:** Codex oturumları arasında promptlar aranabilirken işlem gözlemleri ve özetler neden görünmüyor?

## Evidence / Kanıtlar

1. Initial tests recorded prompts only in the local Viewer. / İlk testlerde Viewer yalnızca promptları gösterdi.
2. Worker health returned HTTP 200, and required doctor checks passed. / Worker HTTP 200 döndürdü, zorunlu doctor kontrolleri geçti.
3. `PostToolUse` was present in the installed Codex plugin hook manifest. Presence alone does not prove execution. / Kurulu hook tanımında `PostToolUse` mevcuttu; tanımlı olmak çalıştığını kanıtlamaz.
4. The configured provider was `claude` while the Claude CLI was absent. / Sağlayıcı `claude` idi, Claude CLI kurulu değildi.
5. Repeated worker warnings showed `dependency=claude_cli`, `status=setup_required`, `Claude executable not found`. / Worker loglarında bu uyarılar tekrarlandı.
6. After changing the provider to `codex`, a fresh synthetic script execution produced two observations and a session summary. / Sağlayıcı `codex` yapıldıktan sonra yeni sentetik testte iki observation ve oturum özeti görüldü.

## Expected versus actual / Beklenen ve gözlenen

| Condition | Expected | Observed |
|---|---|---|
| Initial `claude` provider, no CLI | Clear installation or runtime guidance; no misleading inference from a healthy Worker | Prompts captured; observer generation skipped with warnings in logs |
| `codex` provider, subsequent synthetic run | Observations and summary available | Two observations and one summary visible |

## Interpretation / Yorum

**EN:** The evidence is consistent with an unmet observer-provider dependency. It does not establish a defect in hook implementation. A UX improvement could detect this condition during setup/diagnostics and present the Codex provider as a supported alternative.

**TR:** Kanıtlar observer sağlayıcısına ait karşılanmamış bir bağımlılıkla uyumludur. Hook kodunda hata olduğunu kanıtlamaz. Kurulum/tanı sırasında bu koşulun tespit edilmesi ve desteklenen Codex sağlayıcısının önerilmesi faydalı olabilir.

## Limitations / Sınırlamalar

- Different synthetic tasks were used before and after; the experiment was not fully controlled.
- Tool-hook invocation and observer queue internals were not instrumented independently.
- No fix or upstream code change has been submitted.

- Önce ve sonra farklı sentetik görevler kullanıldı; deney tam kontrollü değildir.
- Hook tetikleme ve observer kuyruğu ayrı ayrı araçlandırılmadı.
- Henüz upstream kod düzeltmesi gönderilmedi.

## Upstream issue / Geliştirici raporu

https://github.com/thedotmack/claude-mem/issues/5359
