<template>
  <v-avatar
    v-if="status === Severity.UNSPECIFIED"
    tile
    color="#666666"
    size="24"
    title="Unspecified"
  >
    <span class="white--text font-weight-bold">U</span>
  </v-avatar>

  <v-avatar
    v-else-if="status === Severity.STYLE"
    tile
    color="#9932cc"
    size="24"
    title="Style"
  >
    <span class="white--text font-weight-bold">S</span>
  </v-avatar>

  <v-avatar
    v-else-if="status === Severity.LOW"
    tile
    color="#669603"
    size="24"
    title="Low"
  >
    <span class="white--text font-weight-bold">L</span>
  </v-avatar>

  <v-avatar
    v-else-if="status === Severity.MEDIUM"
    tile
    color="#a9d323"
    size="24"
    title="Medium"
  >
    <span class="white--text font-weight-bold">M</span>
  </v-avatar>

  <v-avatar
    v-else-if="status === Severity.HIGH"
    tile
    color="#ffa800"
    size="24"
    title="High"
  >
    <span class="white--text font-weight-bold">H</span>
  </v-avatar>

  <v-avatar
    v-else-if="status === Severity.CRITICAL"
    tile
    color="#e92625"
    size="24"
    title="Critical"
  >
    <span class="white--text font-weight-bold">C</span>
  </v-avatar>
</template>

<script>
import { Severity } from "@cc/report-server-types";

export default {
  name: "SeverityIcon",
  props: {
    status: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      Severity
    };
  }
};
</script>
