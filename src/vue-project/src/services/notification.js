import { toast } from "./primevue";

export function showNotification(
  title = "Title Here",
  message = "Message Here",
  severity = "info", // success, info, warn, error
  duration = 2000
) {
  toast.add({
    severity: severity,
    summary: title,
    detail: message,
    life: duration,
  });
}
