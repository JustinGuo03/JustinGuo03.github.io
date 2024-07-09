export interface Word {
    id: number | null;
    word: string;
    letter1: string;
    letter2: string;
    letter3: string;
    letter4: string;
    letter5: string;
    score: number;
  }

export interface DataFrame {
  [key: string]: string;
  word: string;
}

export class Counter<T> {
  private counts: Map<T, number>;

  constructor() {
      this.counts = new Map<T, number>();
  }

  update(items: T[]): void {
      for (const item of items) {
          this.counts.set(item, (this.counts.get(item) || 0) + 1);
      }
  }

  get(item: T): number {
      return this.counts.get(item) || 0;
  }
}