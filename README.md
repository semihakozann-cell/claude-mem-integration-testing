# Claude-Mem × Codex CLI Integration Testing

**Reproducible integration QA case study | Tekrarlanabilir entegrasyon testi**

This repository documents a real-world investigation of local memory generation in Claude-Mem v15.9.0 with Codex CLI v0.166.0 on Apple Silicon macOS. It is an independent test case study, **not** an official Claude-Mem project or a claim that its `PostToolUse` implementation is broken.

Bu depo, Apple Silicon macOS üzerinde Claude-Mem v15.9.0 ile Codex CLI v0.166.0 kullanılırken yerel hafıza oluşturma davranışının incelenmesini belgeler. Resmî Claude-Mem projesi değildir; `PostToolUse` kodunda hata kanıtlandığı iddia edilmez.

## Related upstream report / İlgili geliştirici raporu

- [Claude-Mem issue #5359](https://github.com/thedotmack/claude-mem/issues/5359)

## Findings / Bulgular

| Check | Before: `CLAUDE_MEM_PROVIDER=claude` (Claude CLI unavailable) | After: `CLAUDE_MEM_PROVIDER=codex` |
|---|---|---|
| Prompt capture | Observed | Observed |
| Tool observations in Viewer | Not observed | Observed (`feature`, `discovery`) |
| Session summaries in Viewer | Not observed | Observed |
| Worker HTTP health | HTTP 200 | Not separately remeasured |
| `doctor` required checks | Passed | Not separately remeasured |

**Interpretation (EN):** Logs repeatedly reported `dependency=claude_cli`, `status=setup_required`, and `Claude executable not found` under the initial provider configuration. A later synthetic execution generated observations and a session summary after changing to `codex`. This supports a provider-configuration/dependency explanation; the separate tasks and other potential state changes mean it is not a controlled causal experiment.

**Yorum (TR):** İlk yapılandırmada loglar sürekli `dependency=claude_cli`, `status=setup_required` ve `Claude executable not found` uyarıları verdi. Sağlayıcı `codex` olarak değiştirildikten sonraki sentetik testte observation ve oturum özeti oluştu. Bu, sağlayıcı/bağımlılık açıklamasını destekler; testler farklı görevlerle yürütüldüğünden tek başına kontrollü nedensellik kanıtı değildir.

## Reproduce / Yeniden üretme

**Prerequisites:** Claude-Mem v15.9.0, Codex CLI v0.166.0 and an isolated scratch directory. Use only synthetic inputs; do not upload sensitive logs, tokens, private paths or client data.

1. Examine the selected local memory provider (do not publish API keys or credentials).
2. In an isolated Codex session, create and execute a small Python script.
3. Check the local Claude-Mem Memory Viewer for prompt, observation and summary entries.
4. Review sanitized worker warnings for missing provider dependencies.
5. If supported and authorized, switch the memory provider from `claude` to `codex`, restart or reload the service, and run a fresh synthetic task.
6. Document both the observed outputs and what was *not* verified.

**Türkçe:** Önce yerel hafıza sağlayıcısını kontrol et; izole dizinde örnek Python görevi çalıştır; Viewer'daki prompt, observation ve summary kayıtlarını karşılaştır; gizli bilgileri ayıklanmış logları incele; desteklenen sağlayıcıya geçiş sonrası yeni test yap. Eksik kanıtları açıkça belirt.

## Included test / Örnek test

`tests/test_memory_math.py` reproduces the deterministic population-standard-deviation calculation. It does **not** automatically test the Claude-Mem hooks; observations must be checked separately in the memory viewer.

```bash
python3 tests/test_memory_math.py
```

## Project structure / Dosya yapısı

- `tests/test_memory_math.py`: deterministic synthetic calculation / deterministik sentetik hesaplama
- `docs/CASE_STUDY.md`: expected-versus-observed QA report / beklenen ve gözlenen sonuç raporu
- `.gitignore`: prevents local logs, secrets and test environment artifacts from being tracked / yerel log ve gizli dosyaları dışlar

## Boundaries / Sınırlar

- No client data, private project files, authentication material or raw debug logs.
- No claim of a submitted or merged Pull Request.
- The upstream issue may be closed as expected configuration behavior; this case study remains useful as a setup-validation test.

**License:** MIT for original content in this repository. Claude-Mem itself is separately licensed by its maintainers.
